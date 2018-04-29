import requests
import datetime
from bs4 import BeautifulSoup
#import config

username = 'uditgulati0'

institute_name = 'NIT Hamirpur'

def get_submissions(user):
	page = requests.get("http://www.spoj.com/status/"+user)

	soup = BeautifulSoup(page.content, 'html.parser')

	sumbissions = {}

	for item in soup.find_all('tr', class_='kol1 '):
		part = item.find(class_="status_sm")
		part2 = part.find('span').get_text()
		d = datetime.datetime.strptime(part2, '%Y-%m-%d %H:%M:%S')
		stamp = d.timestamp()
		part3 = item.find(class_="sproblem text-center")
		part4 = part3.find('a')
		prob_name = part4["title"]
		#print(int(stamp), prob_name)
		sumbissions[int(stamp)] = prob_name

	return sumbissions


def get_rank(user):
	page = requests.get("http://www.spoj.com/users/"+user)
	soup = BeautifulSoup(page.content, 'html.parser')

	rank = 0
	details = []

	item = soup.find('div', class_='col-md-3')
	for point in item.find_all('p'):
		#print(point)
		text = point.get_text()
		details.append(text)
	#print(details)
	
	rank_text = details[2]
	#print(rank_text)
	
	flag = False
	temp = ''
	for char in rank_text:
		if char == '#':
			flag = True
		if char == ' ':
			flag = False
		if flag == True and char != '#':
			temp += char
	rank = int(temp)
	#print(rank)
	return rank


def fetch_submissions():
	users = [line.rstrip('\n') for line in open('scrapers/users1.txt')]
	for user in users:
		dict = get_submissions(user)
		print(dict)


def fetch_ranks():
	ranks = []
	users = [line.rstrip('\n') for line in open('scrapers/users1.txt')]
	for user in users:
		curr = get_rank(user)
		ranks.append((curr, user))
		#print(dict)

	ranks.sort()
	return ranks


def fetch_data():
	fetch_submissions()
	fetch_ranks()
