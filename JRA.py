#最初にやったPyConのスポンサーのスクレイピングを改造したコードです

import requests
from bs4 import BeautifulSoup

#空白を削除(not-use)
def remove_whitespace (str):
	return ''.join(str.split())

def main():
	url = 'https://race.sp.netkeiba.com/?pid=shutuba&race_id=201905010211'
	res = requests.get(url)
	content = res.content
	soup = BeautifulSoup(content, 'html.parser')
	#soupに人気取得のための別名を付けてみた
	popular_soup = soup

	#スクレイピングしたデータの処理
	#必要に応じてコメントアウト
	#write_soup_file(soup)
	
	#競走名を取得する
	get_race_title(soup)

	get_Horse_name(soup)

#レース名を取得したい
def get_race_title(sup):
	race_title = sup.find('dt', class_='Race_Name')
	#改行コードだけの変数を作って、無理矢理改行させる
	return_code = "\n"
	
	#取得したレース名のテキストから空白文字を削除
	print( race_title.text.strip() )

	write_horce_info( race_title.text.strip() )
	write_horce_info(return_code)

def get_Hoarce_popular(sup):
	popularn = sup.find_all('td', class_='Poppular')



def get_Horse_name(sup):
	horce_name = sup.find_all('tr', class_='HorseList')
	#まだ書いてる途中
	#馬番や印なんかを取得したい
	#numbers = sup.find_all(
	#marking = soup.find_all('
	for sponsor in horce_name:
		#url = sponsor.text
		name = sponsor.a.text
		print(name)
		#型確認
		#print(type(name))

		write_horce_info(name)

def write_soup_file(sop):
	with open(path_prt, mode = 'w') as p:
		p.write(str(sop))
	
def write_horce_info(name):
	#最初に区切り線なんかを入れたいよね
	#レース名とか
	horce_file = open(path_w, mode = 'a')
	#改行コードだけの変数を作って、無理矢理改行させる
	return_code = "\n"

	horce_file.writelines( str(name) )
	horce_file.write(return_code)

	horce_file.close()

#整形済みのsoup内のデータを表示させる
def debug_soup_property(property_name):
	print(property_name.prettify())


if __name__ == '__main__':
	path_w = './JRAHorse.txt'
	path_prt = './SoupPrettify.txt'

	main()


