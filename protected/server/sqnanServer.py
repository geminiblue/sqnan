#encoding=utf-8

import sqlite3

from ConfigParser import ConfigParser
from models import *
from pub.Tools import Tools
from pub.LogInfo import LogInfo
import top.api
import top
import redis

req=top.api.TaobaokeItemsGetRequest("gw.api.taobao.com",80)
appkey="21202201"
secret="your54bd434afb6cb8b81bf083efd3f5555f"
req.set_app_info(top.appinfo(appkey,secret))
req.fields="num_iid,title,nick,pic_url,price,click_url,commission,commission_rate,commission_num,commission_volume,shop_click_url,seller_credit_score,item_location,volume"
req.cid=30
req.nick="490997183_qq_com"
try:
	resp= req.getResponse()
	print(resp)
except Exception,e:
	print(e)

