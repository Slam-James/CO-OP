from bs4 import BeautifulSoup
import urllib.request
import lxml
import re

r = urllib.request.urlopen('https://www.eventective.com/ottawa-on/meeting-venues/?p=1-2').read()
soup = BeautifulSoup(r, 'html.parser')  # Use 'html.parser' instead of 'xml' for HTML parsing

file = open("Scraper.txt", "w")
for body in soup.find_all('a'):
    href = body.get('href')
    if href:
        print(href)
        print(body.get_text())
        print(soup.prettify()[0:10000])
        file.write(href + '\n')  # Write href to the file and add a newline character
file.flush()
file.close()  # Call the close function with parentheses
