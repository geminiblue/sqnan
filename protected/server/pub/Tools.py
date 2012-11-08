#encoding=utf-8
import threading
import hashlib
import os,sys,time
mylock = threading.RLock()
class Tools():
    @staticmethod
    def getNow():
        '''
        ���ص�ǰʱ���
        @return:int
        '''
        mylock.acquire()
        tmpTime = int(time.time())
        mylock.release()
        return tmpTime

    @staticmethod
    def md5(sStr):
        '''
        �����ַ�����md5����
        @param sStr:string  Ҫ���ܵ��ַ���
        @return:string ���ܺ���ַ���
        '''
        if sStr!="":
            return hashlib.md5(sStr).hexdigest()
    @staticmethod
    def fNow():
        '''
        ���ظ�ʽ�����ʱ��
        '''
        return time.strftime("%Y - %m - %d %H:%M:%S",time.gmtime())