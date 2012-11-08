#encoding=utf-8

import sqlite3

from ConfigParser import ConfigParser
from models import *
from pub.Tools import Tools
from pub.LogInfo import LogInfo
if __name__=="__main__":
    print Tools.getNow()
    print Tools.md5("geminiblue")
    try:
        w=n
    except Exception,ex:
        LogInfo.writeLog("error",ex)