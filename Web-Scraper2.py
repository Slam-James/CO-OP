import requests as re
from bs4 import BeautifulSoup

URL = "https://www.eventective.com/ottawa-on/meeting-venues/?p=1-2"
page = re.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find_all('a')

for result in results:
    print(result.text.strip())
