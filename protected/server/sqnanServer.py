#encoding=utf-8

import sqlite3

from ConfigParser import ConfigParser
from models import *
from pub.Tools import Tools
from pub.LogInfo import LogInfo
import top.api
import top
import redis,json

r = redis.StrictRedis(host='localhost', port=10021)
url="gw.api.taobao.com"
port=80
appkey="21202201"
secret="54bd434afb6cb8b81bf083efd3f5555f"
req=top.api.TaobaokeItemsGetRequest(url,port)
req.set_app_info(top.appinfo(appkey,secret))

req.fields="num_iid,title,nick,pic_url,price,click_url,commission,commission_rate,commission_num,commission_volume,shop_click_url,seller_credit_score,item_location,volume"
req.nick="490997183_qq_com"
req.cid=30
req.format="json"
req.page_no=1
req.page_size=40
try:
	resp= req.getResponse()
	if(resp!=None):
		AllData = resp["taobaoke_items_get_response"]["taobaoke_items"]
		#print AllData
		tmpKey=[]
		for data in AllData["taobaoke_item"]:
			volume = data["volume"]
			#print volume
			tmpKey.append(volume)
			nick = data["nick"]
			item_location = data["item_location"]
			title = data["title"]
			price = data["price"]
			click_url = data["click_url"]
			pic_url = data["pic_url"]
			str = '{nick:"%s",title:"%s",click_url:"%s",pic_url:"%s"}'%(nick,title,click_url,pic_url)
			print volume
			r.set(volume,str)
		r.set("TOPKELASTKEYS",tmpKey)
		print r.get("TOPKELASTKEYS")
except Exception,e:
	print(e)

