import requests
import datetime
from bs4 import BeautifulSoup

def get_rank(user):
	page = requests.get("https://www.codechef.com/users/"+user)
	soup = BeautifulSoup(page.content, 'html.parser')
	list =[]
	for item in soup.find_all('div',class_ = 'rating-ranks'):
		for var in item.find_all('a'):
			rank = int(var.string)
			list.append(rank)
			
	return list		


def get_rating(user):
	page = requests.get("https://www.codechef.com/users/"+user)
	soup = BeautifulSoup(page.content, 'html.parser')
	rating =0
	for item in soup.find_all('div',class_='rating-number'):
		rating = int(item.get_text())
	return rating		


def fetch():
	users = [line.rstrip('\n') for line in open('user2.txt')]
	for user in users:
		dic = {}
		dic['username'] = user
		list = get_rank(user)
		rank1 = list[0]
		rank2 = list[1]
		dic['global_rank'] = max(rank1,rank2)
		dic['country_rank' ]= min(rank1,rank2)
		dic['rating'] = get_rating(user)
		print(dic)
if __name__ == '__main__':
	fetch()
							
