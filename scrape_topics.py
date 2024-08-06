import requests
from bs4 import BeautifulSoup
import time

def get_card_links(page_number):
    url = f"https://mitreden.braunschweig.de/ideenplattform?page={page_number}#idea-list"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Find all links within <ul class="links"> and <h3 class="title">
        link_elements = soup.select('ul.links a, h3.title a')
        links = {link['href'] for link in link_elements if 'href' in link.attrs}
        return links
    else:
        return set()

def get_card_details(link):
    full_url = f"https://mitreden.braunschweig.de{link}"
    response = requests.get(full_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract title
        title_element = soup.find('meta', property='og:title')
        title = title_element['content'].strip() if title_element else 'No Title'

        # Extract description from the specific div with class 'field-item'
        description_element = soup.find('div',
                                        class_='field-item field-item--text_with_summary field-item--body field-item--node')
        description = description_element.get_text(strip=True) if description_element else 'No Description'

        # Extract status
        status_element = soup.find('span', class_='status-name')
        status = status_element.text.strip() if status_element else 'No Status'

        # Extract tag
        tag_element = soup.find('div', class_='badge')
        tag = tag_element.text.strip() if tag_element else 'No Tag'

        # Extract vote count
        vote_element = soup.find('div', class_='quorum-counter')
        vote = vote_element.text.strip() if vote_element else 'No Vote Count'

        return title, description, status, tag, vote
    else:
        return None, None, None, None, None




if __name__ == "__main__":


    all_links = set()
    for page_number in range(11):  # Loop through the first 11 pages
        links = get_card_links(page_number)
        all_links.update(links)

    card_details = []

    for link in all_links:
        title, description, status, tag, vote = get_card_details(link)
        if title and description:
            card_details.append({
                'title': title,
                'description': description,
                'status': status,
                'tag': tag,
                'vote': vote
            })

    import json
    # Save the details to a JSON file
    with open('card_details.json', 'w', encoding='utf-8') as json_file:
        json.dump(card_details, json_file, ensure_ascii=False, indent=4)



    # all_cards = []
    #
    #
    # for page_number in range(0,11):
    #     # construct the URL
    #     url = f"https://mitreden.braunschweig.de/ideenplattform?page={page_number}#idea-list"
    #     # Make a request to the page
    #     response = requests.get(url)
    #
    #     # check if the request was successful
    #     if response.status_code == 200:
    #         # Parse the page content
    #         soup = BeautifulSoup(response.content, 'html.parser')
    #         # Find all the cards on the page
    #         cards = soup.find_all(class_='field-item field-item--string field-item--title field-item--node')  # Adjust the class name to match the website)
    #         # Extract the hpyerlinks from the cards



        # for card in cards:
        #     title = card.find('h3').text.strip()
        #     description = card.find('p').text.strip()
        #     all_cards.append({
        #         "title": title,
        #         "description": description
        #     })




    # # Set up Selenium WebDriver
    # options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # Run in headless mode (no GUI)
    # driver = webdriver.Chrome(options=options)
    #
    # # Open the website
    # driver.get(url)
    #
    # # Wait for the page to load
    # wait = WebDriverWait(driver, 10)
    # wait.until(EC.presence_of_element_located((By.CLASS_NAME, "idea-container")))  # Adjust the class name as needed
    #
    # # Scroll to load more items if necessary
    # last_height = driver.execute_script("return document.body.scrollHeight")
    # while True:
    #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #     time.sleep(2)  # Wait for new content to load
    #     new_height = driver.execute_script("return document.body.scrollHeight")
    #     if new_height == last_height:
    #         break
    #     last_height = new_height
    #
    # # Parse the loaded content with BeautifulSoup
    # soup = BeautifulSoup(driver.page_source, 'html.parser')
    #
    # # Close the WebDriver
    # driver.quit()
    #
    # # Find all topics
    # topics = soup.find_all('div', class_='idea-container')  # Adjust the class name as needed
    #
    # # Extract and print topic information
    # for topic in topics:
    #     title = topic.find('h3').text.strip()  # Adjust the tag and class name as needed
    #     description = topic.find('p').text.strip()  # Adjust the tag and class name as needed
    #     print(f"Title: {title}")
    #     print(f"Description: {description}")
    #     print("------")
    #
    # # Optionally, save the data to a file or a database
