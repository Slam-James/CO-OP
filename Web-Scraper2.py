import requests as re
from bs4 import BeautifulSoup

URL = "https://www.eventective.com/ottawa-on/wedding-venues/"
page = re.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

results = soup.find_all('a', href=True)

for result in results:
    text = result.text.strip()
    href = result['href']
    if text:  # skip empty anchors
        print(f"{text} -> {href}")
