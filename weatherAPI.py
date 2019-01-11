#参考URL::
#https://qiita.com/shunyooo/items/b408b8d61f9f73b21da7
import requests
import json
import pdb

#set API keys
apikey = 'a4fa204e081b39146d7db2e9fc712344'

cities = ['Tokyo, JP', 'Sakata, JP']

url = 'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}'

k2c = lambda k: k - 273.15

#各都市の温度を取得

for city in cities:
		#get API url
		api_url = url.format(city=city, key=apikey)
		res = requests.get(api_url)
		#JSON形式でないならエラー吐く
		#dict形式
		data = json.loads(res.text)
		pdb.set_trace()

		#output
		print('+ 都市=', data['name'])
		print('| 天気=', data['weather'][0]['description'])
		print('| 最低気温=', k2c(data['main']['temp_min']))
		print('| 最高気温=', k2c(data['main']['temp_max']))
