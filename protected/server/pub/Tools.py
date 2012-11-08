#encoding=utf-8
import threading
import hashlib
import os,sys,time
mylock = threading.RLock()
class Tools():
    @staticmethod
    def getNow():
        '''
        返回当前时间戳
        @return:int
        '''
        mylock.acquire()
        tmpTime = int(time.time())
        mylock.release()
        return tmpTime

    @staticmethod
    def md5(sStr):
        '''
        返回字符串的md5加密
        @param sStr:string  要加密的字符串
        @return:string 加密后的字符串
        '''
        if sStr!="":
            return hashlib.md5(sStr).hexdigest()
    @staticmethod
    def fNow():
        '''
        返回格式化后的时间
        '''
        return time.strftime("%Y - %m - %d %H:%M:%S",time.gmtime())