import requests
import datetime
from bs4 import BeautifulSoup



def codechef():
	page = requests.get("https://www.codechef.com/contests")
	soup = BeautifulSoup(page.content, 'html.parser')

	table = soup.find(class_ = 'dataTable')
	flag = False
	contests = []

	for row in table.find_all('tr'):
		if flag:
			temp = []
			for col in row.find_all('td'):
				data = col.get_text().strip()
				temp.append(data)

			contests.append(tuple(temp));

		flag = True

	return contests

def codeforces():
	page = requests.get("http://codeforces.com/contests")
	soup = BeautifulSoup(page.content, 'html.parser')

	table = soup.find('table')
	flag = False
	contests = []

	for row in table.find_all('tr'):
		if flag:
			temp = []
			for col in row.find_all('td'):
				data = col.get_text().strip()
				temp.append(data)

			contests.append((temp[0], temp[2], temp[3]))

		flag = True

	return contests


def fetch_data():
	codechef()
	codeforces()