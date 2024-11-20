import csv
import time
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
        listing_position = 1
        for item in items[:20]:
            try:
                title = item.find_element(By.CSS_SELECTOR, ".s-item__title").text
                seller = item.find_element(By.CSS_SELECTOR, ".s-item__seller-info-text").text
                price = item.find_element(By.CSS_SELECTOR, ".s-item__price").text

                results.append({
                    "position": listing_position,
                    "title": title,
                    "seller": seller,
                    "price": price
                })

                listing_position += 1
            except Exception as e:
                continue

        return results

    finally:
        driver.quit()


def read_queries_from_csv(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        csv_reader = csv.DictReader(file)
        queries = [row["ebay_query"] for row in csv_reader]
    return queries

if __name__ == "__main__":
    csv_file_path = "queries.csv"
    search_terms = read_queries_from_csv(csv_file_path)

    for term in search_terms:
        print(f"Scraping result for query: {term}")


        data = scrape_ebay(term)
        for entry in data:
            print(
                f"Position: {entry['position']},"
                f"Title: {entry['title']},"
                f"Seller: {entry['seller']},"
                f"Price: {entry['price']}"
            )
            time.sleep(5)
