from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from webdriver_manager.firefox import GeckoDriverManager


def scrape_ebay(query):
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    try:
        driver.get(f"https://www.ebay.co.uk/sch/i.html?_nkw={query}")

        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR, ".s-item"))
        )

        items = driver.find_elements(By.CSS_SELECTOR, ".s-item")

        results = []
        for item in items[:20]:
            try:
                title = item.find_element(By.CSS_SELECTOR, ".s-item__title").text
                seller = item.find_element(By.CSS_SELECTOR, ".s-item__seller-info-text").text
                price = item.find_element(By.CSS_SELECTOR, ".s-item__price").text

                results.append({
                    "title": title,
                    "seller": seller,
                    "price": price
                })

            except Exception as e:
                continue

        return results

    finally:
        driver.quit()


if __name__ == "__main__":
    search_query = "vw golf 2016 mirror glass"
    data = scrape_ebay(search_query)

    for entry in data:
        print(
            f"Title: {entry['title']},"
            f"Seller: {entry['seller']},"
            f"Price: {entry['price']}"
        )
