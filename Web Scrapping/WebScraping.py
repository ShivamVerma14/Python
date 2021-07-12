import requests
import bs4
from requests.api import request

'''result = requests.get("http://www.example.com")

soup = bs4.BeautifulSoup(result.text, 'lxml')

# Grabbing the title of the domain
print(soup.select('title')[0].getText())

res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')

soup = bs4.BeautifulSoup(res.text, 'lxml')

# Grabbing text of Table of Contents
for item in soup.select('.toctext'):
    print(item.text)'''

request = requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')

soup = bs4.BeautifulSoup(request.text, 'lxml')

image_link = requests.get('https:' + soup.select('.thumbimage')[0]['src'])

with open('my_image.jpg', 'wb') as file:
    file.write(image_link.content)