from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import csv

# States to scrape
states = ["texas", "oklahoma", "arkansas", "louisiana", "tennessee",
          "alabama", "mississippi", "florida", "georgia"]

# Base URL
base_url = "https://www.cloudtango.net/directory/"

# Setup headless Chrome
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)

# Store results
msp_data = []

for state in states:
    print(f"Scraping {state.title()} MSPs...")
    url = f"{base_url}{state}/"
    driver.get(url)
    time.sleep(3)

    listings = driver.find_elements(By.CSS_SELECTOR, ".company-listing")

    for listing in listings:
        try:
            name = listing.find_element(By.CSS_SELECTOR, ".company-name").text
            location = listing.find_element(By.CSS_SELECTOR, ".company-location").text
            profile_url = listing.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
            msp_data.append([state.title(), name, location, profile_url])
        except Exception:
            continue

driver.quit()

# Save to CSV
with open("cloudtango_msp_listings.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["State", "Company Name", "Location", "Profile URL"])
    writer.writerows(msp_data)

print("✅ Scraping complete. Data saved to cloudtango_msp_listings.csv")
