import requests
from bs4 import BeautifulSoup
#pdbデバッガをインポートしておく
import pdb

def main():
	url = 'https://pycon.jp/2017/ja/sponsors/'
	res = requests.get(url)
#デバッガ文
	#pdb.set_trace()
	content = res.content
	soup = BeautifulSoup(content, 'html.parser')
	sponsors = soup.find_all('div', class_='sponsor-content')
	for sponsor in sponsors:
		url = sponsor.h3.a['href']
		name = sponsor.h4.text
		print(name, url)


if __name__ == '__main__':
	main()
