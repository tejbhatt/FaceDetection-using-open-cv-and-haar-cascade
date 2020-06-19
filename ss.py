import requests
from bs4 import BeautifulSoup
import urllib

url = 'https://www.reddit.com/r/funny'

response = requests.get(url)

soup = BeautifulSoup(response.content,"html.parser")

images = soup.find_all('img')

#print(images)

number = 0

for image in images:
    images_src = image["src"]
    urlib.request.urlretrieve(image_src,str(number))
    number = number+1
