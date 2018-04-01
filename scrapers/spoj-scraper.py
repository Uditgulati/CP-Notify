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


def fetch():
	users = [line.rstrip('\n') for line in open('users1.txt')]
	for user in users:
		dict = get_submissions(user)
		print(dict)

	print()
	

if __name__ == '__main__':
	fetch()
