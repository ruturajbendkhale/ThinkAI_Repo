import os
from dotenv import load_dotenv
from firecrawl import FireCrawlApp


def scrape_data(url):
    load_dotenv()

    app = FireCrawlApp(api_key=os.getenv("FIRECRAWL_API_KEY"))

    # Scrape the data
    scraped_data = app.scrape_url(url)

    # check if markdown key is present in the scraped data
    if "markdown" in scraped_data:
        # Print the markdown content
        return scraped_data["markdown"]
    else:
        raise Exception("Markdown content not found in the scraped data")


def save_data(raw_data, datetime, output_folder="output"):
    os.makedirs(output_folder, exist_ok=True)

    raw_output_path = os.path.join(output_folder, f"raw_data_{datetime}.json")
    with open(raw_output_path, "w", encoding='utf-8') as f:
        f.write(raw_data)
    print(f"Raw data saved to: {raw_output_path}")
