# pakwheels_scraper.py

from bs4 import BeautifulSoup
import requests
import pandas as pd
import time

# Headers for request
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'
}

# Base URL for Karachi Cars (10 pages)
base_url = "https://www.pakwheels.com/used-cars/karachi/24857?page={}"

# Storage for all scraped cars
all_cars = []

print("Starting Scraping...\n")

for page in range(1, 11):  # Scrape pages 1 to 10
    print(f"Scraping page {page}...")
    url = base_url.format(page)

    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")

    # All car cards
    cards = soup.find_all("div", class_="col-md-9 grid-style")

    for card in cards:

        # Car title
        title_tag = card.find("h3")
        title = title_tag.text.strip() if title_tag else None

        # Ratings
        rating_tag = card.find("span", class_="rating-stars")
        ratings = rating_tag.text.strip() if rating_tag else None

        # Price
        price_tag = card.find("div", class_="price-details")
        price = price_tag.text.strip() if price_tag else None

        # UL List
        ul = card.find("ul", class_="list-unstyled search-vehicle-info-2 fs13")
        li_list = [li.text.strip() for li in ul.find_all("li")] if ul else []

        # Extract values safely
        car_info = {
            "title": title,
            "ratings": ratings,
            "price": price,
            "year": li_list[0] if len(li_list) > 0 else None,
            "mileage": li_list[1] if len(li_list) > 1 else None,
            "fuel": li_list[2] if len(li_list) > 2 else None,
            "engine": li_list[3] if len(li_list) > 3 else None,
            "transmission": li_list[4] if len(li_list) > 4 else None,
            "grade": li_list[5] if len(li_list) > 5 else None
        }

        all_cars.append(car_info)

    time.sleep(1)  # Delay to avoid blocking

print("\nScraping Completed Successfully!")

# Convert to DataFrame
df = pd.DataFrame(all_cars)

# Save CSV
df.to_csv("pakwheels_10_pages.csv", index=False)

# Save JSON
df.to_json("pakwheels_10_pages.json", orient="records", lines=True)

print("Files Saved:")
print(" - pakwheels_10_pages.csv")
print(" - pakwheels_10_pages.json")
