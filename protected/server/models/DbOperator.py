#encoding=utf8
'''
Created on 2012-9-24

@author: Administrator
'''
import sys,os
try:
    from DBUtils.PooledDB import PooledDB
    from mysql.connector import errorcode
    import mysql.connector
    from pub.Config import Config
    from pub.LogInfo import LogInfo
except ImportError,ex:
    print ex
    sys.exit()
cfg = {
#           鏁版嵁搴撹繛鎺ラ厤缃�
       "DbConnectString" :{
                                            'user': 'root',
                                            'password': '123456',
                                            'host': 'localhost',
                                            'database': 'sqnan',
                                            'raise_on_warnings': True, },

}

class Singleton(object):   
    def __new__(cls): 
        import threading   
        mylock = threading.RLock()   
        mylock.acquire()   
        cls.instance = object.__new__(cls)   
        cls.__new__ = cls.Instance   
        cls.instance.init()
        mylock.release()
        return cls.instance
    @classmethod   
    def Instance(cls, type):   
        return cls.instance   
    def init(self):   
        pass
#encoding=utf8
'''
Created on 2012-9-17

@author: Administrator
'''

class DbManager(Singleton):
    '''
    鏁版嵁搴撹繛鎺ユ睜瀵硅薄
    '''
    def __init__(self):
        self.__pool = PooledDB(mysql.connector,mincached=0, maxcached=10, maxshared=10, maxusage=10000, **cfg["DbConnectString"])
    def getConnection(self):
        '''
        浠庤繛鎺ユ睜涓彇鍑虹殑鏁版嵁杩炴帴瀵硅薄
        '''
        return self.__pool.connection()

class DbOperator():
    '''
    '''

    def __init__(self):
        try:
            self.__dbHandle = DbManager().getConnection()
            self.__cursor = self.__dbHandle.cursor()
        except mysql.connector.Error as err:
            return self.__dbError(err)
            sys.exit()
    def __del__(self):
        try:
            self.__cursor.close()
            self.__cursor = None
            self.__dbHandle.close()
            self.__dbHandle = None
        except:
            pass
    def query(self):
        pass
    def findByPK(self,Sql):
        try:
            self.__cursor.execute(Sql)
            return self.__cursor.fetchone()
        except mysql.connector.Error as err:
            return self.__dbError(err)
    def getCursor(self):
        return self.__cursor
    def getOne(self,Sql):
        try: 
            self.__cursor.execute(Sql)
            result = self.__cursor.fetchone()
            if(result!=None):
                return dict(zip(self.__cursor.column_names, result))
            else:
                return Config.S_SYS_NONE
        except mysql.connector.Error as err:
            return self.__dbError(err)
    def getFieldByCondition(self,aParam):
        '''
        鏍规嵁鏉′欢鏌ヨ鍐呭
        '''
        resultRow = 1
        if(aParam!=None):
            sSql = " SELECT %s FROM %s WHERE 1=1  AND %s "
            condition = " AND 1=1 "
            SearchFields = " * "
            if( aParam.has_key(Config.S_SEARCHFIELDS) and  aParam[Config.S_SEARCHFIELDS]!=""):
                SearchFields=aParam[Config.S_SEARCHFIELDS]
            if(aParam.has_key(Config.S_SEARCHCONDITION) and aParam[Config.S_SEARCHCONDITION]!=""):
                condition=aParam[Config.S_SEARCHCONDITION]
            if(aParam.has_key(Config.S_RESULTROW) and aParam[Config.S_RESULTROW]>1):
                resultRow=aParam[Config.S_RESULTROW]

            sSql = sSql % (SearchFields,aParam[Config.S_TABLE],condition)
#            Func.debugInfo(sSql)
            if(aParam.has_key(Config.S_ORDERBY) and aParam[Config.S_ORDERBY]!=""):
                sOrderBy = aParam[Config.S_ORDERBY]
                sSql = sSql+(" ORDER BY %s" % sOrderBy )
            if(aParam.has_key(Config.S_LIMIT) and aParam[Config.S_LIMIT]!=""):
                sLimit = aParam[Config.S_LIMIT]
            else:
                sLimit = " 1 ";
            if(aParam.has_key(Config.S_FETCH_ALL) and aParam[Config.S_FETCH_ALL]==False):
                    sSql = sSql + (" LIMIT %s"%sLimit)
            Func.debugInfo(sSql)
            if(resultRow>1):
                return self.findAll(sSql)
            else:
                return self.getOne(sSql)
        else:
            return None
    def findAll(self,Sql=None):
        try:
            self.__cursor.execute(Sql,)
            tmp = self.__cursor.fetchall()
            result = []
            if(tmp!=None):
                for tt in tmp:
                    result.append(dict(zip(self.__cursor.column_names,tt )))
            return result
        except mysql.connector.Error as err:
            return self.__dbError(err)
    def doExecute(self,sSql):
        '''
                        鎵ц涓€鏉ql璇彞锛屽苟杩斿洖鎵€褰卞搷鐨勮鏁�     
        @aParam 
        '''
        if not sSql:
            return 0;
        try:
            self.__cursor.execute(sSql);
#            print self.__cursor.execute(sSql);
            self.__dbHandle.commit()
            return 1
        except mysql.connector.Error as err:
            return self.__dbError(err)
    
    def executeAndGetId(self,Sql,Param=None):
        '''
                        鎵цSql璇彞骞惰繑鍥為€掑Id
        @param Sql:瑕佹墽琛岀殑Sql璇彞
        @param Param:Sql璇彞涓墍瑕佷娇鐢ㄧ殑鍙傛暟
        @return:int  
        '''
        try:
            if Param == None:  
                self.__cursor.execute(Sql)  
            else:  
                self.__cursor.execute(Sql, Param)
            self.__dbHandle.commit()
            return self.__cursor.lastrowid 
        except mysql.connector.Error as err:
            return self.__dbError(err)
    def doInsert(self,aParam):
        if not aParam:
            return None;
        if not aParam.has_key(Config.S_TABLE):
            return None;
        if not aParam.has_key(Config.S_SEARCHFIELDS):
            return None;
        if aParam[Config.S_SEARCHFIELDS]=="":
            return None;
        if aParam[Config.S_SEARCHFIELDS]=="*":
            return None;
        
        
        
        fields="";
        values="";
        fieldsArr=aParam[Config.S_SEARCHFIELDS].split(",")
        for item in fieldsArr:
            tmp=item.split("=");
            fields=fields+str(tmp[0])+",";
            values=values+str(tmp[1])+",";
        fields=fields[:len(fields)-1];
        values=values[:len(values)-1];
        
        
        
        sSql="insert into %s (%s) values(%s)" %(aParam[Config.S_TABLE],fields,values);

        return self.executeAndGetId(sSql); 
        
    
    def doUpdate(self,aParam):
        if not aParam:
            return None;
        if not aParam.has_key(Config.S_TABLE):
            return None;
        if not aParam.has_key(Config.S_SEARCHFIELDS):
            return None;
        if aParam[Config.S_SEARCHFIELDS]=="":
            return None;
        if aParam[Config.S_SEARCHFIELDS]=="*":
            return None;
        
#        sFields=aParam[Config.S_SEARCHFIELDS].replace(",","=%s,")+"=%s";
        sSql="update %s set %s where 1=1" %(aParam[Config.S_TABLE],aParam[Config.S_SEARCHFIELDS]);
        if aParam.has_key(Config.S_SEARCHCONDITION) and aParam[Config.S_SEARCHCONDITION]!="":
            sSql=sSql+" and "+aParam[Config.S_SEARCHCONDITION];
        return self.executeAndGetId(sSql);    
        
        
        
    def doDelete(self,aParam):
        if not aParam:
            return None;
        if not aParam.has_key(Config.S_TABLE):
            return None;
        sSql="DELETE FROM %s where 1=1" %(aParam[Config.S_TABLE]);
        if aParam.has_key(Config.S_SEARCHCONDITION) and aParam[Config.S_SEARCHCONDITION]!="":
            sSql=sSql+" and "+aParam[Config.S_SEARCHCONDITION];
        return self.doExecute(sSql);       
        
    def doSelect(self):
        pass
    def __dbError(self,msg):
        LogInfo.writeLog("error",msg)
        return None
if __name__ == '__main__':
    db=DbOperator();
    aParam={"table":'Sq_UserInfo',"SearchFields":"username='sss'","SearchCondition":"cc='cc'"}
    db.doInsert(aParam);
