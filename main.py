import requests
from bs4 import BeautifulSoup
import re
import webbrowser

def openVideo(name):
    
    # Fetching the HTML content
    response = requests.get("https://www.youtube.com/results?search_query=" + name)

    # Check if the request was successful
    if response.status_code == 200:
        html_content = response.text

        # Parsing the HTML content
        soup = BeautifulSoup(html_content, 'html.parser')

        # Extracting video IDs using regex
        video_ids = re.findall(r"watch\?v=([a-zA-Z0-9_-]{11})", soup.prettify())
        url = "https://www.youtube.com/watch?v=" + video_ids[0]
        webbrowser.open(url)
    else:
        print("Failed to retrieve the web page. Status code:", response.status_code)


if __name__ == '__main__':
    while True:
        name = input("Kvo shte gledame: ")
        openVideo(name)
        # "ctrl + c" to stop