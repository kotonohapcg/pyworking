import requests
from bs4 import BeautifulSoup

def remove_whitespace (str):
	return ''.join(str.split())

def main():
	url = 'https://race.sp.netkeiba.com/?pid=shutuba&race_id=201906010308'
#中山大障害出馬id=201806050710
	res = requests.get(url)
	content = res.content
	soup = BeautifulSoup(content, 'html.parser')
	write_soup_file(soup)
	#debug_soup_property(soup)
	get_Horse_name(soup)

def get_Horse_name(sup):
	sponsors = sup.find_all('tr', class_='HorseList')
	#まだ書いてる途中
	#馬番や印なんかを取得したい
	#numbers = sup.find_all(
	#marking = soup.find_all('
	for sponsor in sponsors:
		#url = sponsor.text
		name = sponsor.a.text
		print(name)
		#型確認
		print(type(name))

		write_horce_name(name)

def write_soup_file(sop):
	with open(path_prt, mode = 'w') as p:
		p.write(str(sop))
	
def write_horce_name(name):
	#最初に区切り線なんかを入れたいよね
	#レース名とか
	horce_file = open(path_w, mode = 'a')
	#改行コードだけの変数を作って、無理矢理改行させる
	returncode = "\n"

	horce_file.writelines( str(name) )
	horce_file.write(returncode)

	horce_file.close()
	
def debug_soup_property(propertyname):
	print(propertyname.prettify())


if __name__ == '__main__':
	path_w = './JRAHorse.txt'
	path_prt = './SoupPrettify.txt'

	main()

