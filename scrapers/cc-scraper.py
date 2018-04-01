import requests
from bs4 import BeautifulSoup
#import config

page = requests.get("http://www.spoj.com/status/uditgulati0/")

print(page.content)
