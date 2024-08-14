import requests
import xml.etree.ElementTree as ET

def fetch_rss_feed(url):
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.content

def parse_rss_feed(xml_content):
    root = ET.fromstring(xml_content)
    items = []
    
    for item in root.findall('.//item'):
        title = item.find('title').text
        description = item.find('description').text
        link = item.find('link').text
        items.append({
            'title': title,
            'description': description,
            'link': link
        })
    
    return items

def display_feed_items(items):
    for item in items:
        print(f"Title: {item['title']}")
        print(f"Description: {item['description']}")
        print(f"Link: {item['link']}")
        print('---')

if __name__ == "__main__":
    url = input("Enter RSS feed URL: ")
    xml_content = fetch_rss_feed(url)
    feed_items = parse_rss_feed(xml_content)
    display_feed_items(feed_items)
