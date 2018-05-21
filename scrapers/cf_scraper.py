import requests
import datetime
from bs4 import BeautifulSoup



def get_rating(user):
	page = requests.get("http://www.codeforces.com/profile/"+user)
	soup = BeautifulSoup(page.content, 'html.parser')

	rating = 0
	details = []

	info = soup.find(class_="info").find('ul').find('li').find('span')

	rating = int(info.get_text())

	return rating


def fetch_ratings():
	ranks = []
	users = [line.rstrip('\n') for line in open('scrapers/users3.txt')]
	for user in users:
		curr = get_rating(user)
		ranks.append((curr, user))
		#print(dict)

	ranks.sort()
	return ranks


def fetch_data():
	#fetch_submissions()
	fetch_ranks()