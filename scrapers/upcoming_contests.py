import requests
import datetime
from bs4 import BeautifulSoup



def codechef():
	pass


def codeforces():
	page = requests.get("http://codeforces.com/contests")
	soup = BeautifulSoup(page.content, 'html.parser')

	table = soup.find('table')

	flag = 0

	contests = []

	for row in table.find_all('tr'):

		if flag:
			#print(row)

			temp = []

			for col in row.find_all('td'):
				data = col.get_text().strip()
				temp.append(data)

			contests.append((temp[0], temp[2], temp[3]))

		flag = 1

	#for x in contests:
	#	print(x)

	return contests


def fetch_data():
	#codechef()
	codeforces()