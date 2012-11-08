#encoding=utf8
'''
Created on 2012-9-28

@author: Administrator

'''
import os
import sys
import time



class Config(object):
    """
        鍏ㄥ眬鍙橀噺绫�,鍏朵腑甯搁噺绫诲瀷涓洪瀛楁瘝浠ｈ〃锛屼緥濡傞瀛楁瘝涓篋鍒欎负瀛楀吀绫诲瀷
        鏁版嵁绫诲瀷璇存槑锛�
        D        瀛楀吀
        I          鏁板瓧
        T        琛�
        S        瀛楃涓�
    """
    CONFIG_KEY_STRING = "sequence_app_configure"
    
#    绯荤粺褰撳墠鏃堕棿甯搁噺
    I_SYS_ZERO = 0
#    绯荤粺闆跺父閲�

    I_SYS_ONE = 1
#    绯荤粺涓€甯搁噺

    S_SYS_NONE = None
#    绯荤粺None甯搁噺
    B_SYS_DEBUG = True
#    绯荤粺璋冭瘯鍙橀噺

#dsaffdfsdfs
    D_USER_DICT = {}
# [Users]
#    鐢ㄦ埛瀛楀吀
#    D_USER_DICT = {
#                 "geminiblue":UserObj,
#                 }

    I_USER_STATE_ONLINE = 1
    #  鐢ㄦ埛鐘舵€�  1 褰撳墠鐢ㄦ埛鍦ㄧ嚎

    I_USER_STATE_OFFLINE = 0
    #  鐢ㄦ埛鐘舵€�  0  褰撳墠鐢ㄦ埛绂荤嚎    
    B_USER_LOGIN_OK = True
    # 鐢ㄦ埛鐧诲綍鎴愬姛
    B_USER_LOGIN_ERR = False
    #鐢ㄦ埛鐧诲綍澶辫触
    I_USER_GAME_STATE_OK = 1
#  鐢ㄦ埛娓告垙鐘舵€�    1 褰撳墠鐢ㄦ埛娓告垙涓�
    I_USER_GAME_STATE_OVER = 0
#  鐢ㄦ埛娓告垙鐘舵€�    0 褰撳墠鐢ㄦ埛琚窐姹�
    I_USER_GAME_STATE_SEE = 2    
#  鐢ㄦ埛娓告垙鐘舵€�    2 鏃佽鐢ㄦ埛锛屼唬琛ㄤ笅灞€鍙弬鍔犳父鎴�

    I_USER_GAME_STATE_INIT= -1;
    #鐢ㄦ埛涓嶅湪浠讳綍鎴块棿閲�
    
    I_USER_IS_ROOM_OWNER = 1
#        褰撳墠鐢ㄦ埛鏄惁鏄埧涓�   1 涓烘槸    
    I_USER_NOT_IS_ROOM_OWNER = 0
#        褰撳墠鐢ㄦ埛鏄惁鏄埧涓�    0 涓哄惁
    I_USER_CHECK_FLAG_YES = 1
#  褰撳墠鐢ㄦ埛琚坊鍔犲ソ鍙嬫椂鏄惁闇€瑕侀獙璇� 1 鏄�
    I_USER_CHECK_FLAG_NO = 0
#  褰撳墠鐢ㄦ埛琚坊鍔犲ソ鍙嬫椂鏄惁闇€瑕侀獙璇� 0 鍚�
    I_USER_SEARCH_FLAG_NONE = 0
#    鏃犳硶鎼滅储鍒扮敤鎴�
    I_USER_SEARCH_FLAG_NICKNAME = 1
#    鍙兘閫氳繃鐢ㄦ埛鍚嶆悳绱㈠埌鐢ㄦ埛
    I_USER_SEARCH_FLAG_USERNAME = 2
#    鍙兘閫氳繃鐢佃瘽鎼滅储鍒�
    I_USER_SEARCH_FLAG_TEL = 4
#    鍙互閫氳繃浠讳綍鏉′欢鎼滅储鍒版鐢ㄦ埛
    I_USER_SEARCH_FLAG_ALL = 8
#    浠讳綍鏉′欢鍙悳绱㈠埌
    I_USER_NOT_FOUND = 1001
#    鐢ㄦ埛鍚嶉敊璇�
    I_USER_PASSWORD_ERROR = 1002
#    鐢ㄦ埛瀵嗙爜閿欒
    I_USER_LOGIN_OK = 1000
#    鐢ㄦ埛鐧诲綍鎴愬姛
    I_USER_REGISTER_OK = 1010
#    鐢ㄦ埛娉ㄥ唽鎴愬姛
    I_USER_REGISTER_USERNAME_FOUND = 1011
#    鐢ㄦ埛娉ㄥ唽鐢ㄦ埛鍚嶅凡瀛樺湪
    I_USER_REGISTER_USERNAME_ERROR = 1012
#    鐢ㄦ埛娉ㄥ唽鐢ㄦ埛鍚嶄笉鍚堟硶
    I_USER_REGISTER_PASSWORD_ERROR = 1013
#    鐢ㄦ埛娉ㄥ唽瀵嗙爜涓嶅悎娉�    
    I_USER_CHANGE_PASSWORD_OK = 1020
#    鐢ㄦ埛淇敼瀵嗙爜鎴愬姛
    I_USER_OLD_PASSWORD_WRONG = 1021
#    鐢ㄦ埛鏃у瘑鐮佷笉绗�
    I_USER_NICK_NAME_FOUND = 1031
#    鐢ㄦ埛鏄电О閲嶅
    I_USER_MODIFAN_INFO_OK = 1030
#    鐢ㄦ埛淇敼淇℃伅鎴愬姛
    I_USER_MODIFAN_INFO_ERROR = 1032
#    鐢ㄦ埛淇敼淇℃伅澶辫触
    D_ROOM_DICT = {}
#  [Rooms]       
#    鎴块棿瀛楀吀
#D_ROOM_DICT = {
#                'roomId':roomObj
#             }    

    I_ROOM_PRI_PUB = 0
    #  鎴块棿鏉冮檺锛�    0  鍏紑鎴块棿
    I_ROOM_PRI_PRO = 1
    #  鎴块棿鏉冮檺锛�   1 绉佹湁鎴块棿

    I_ROOM_TYPE_SYSTEM = 0
    #  鎴块棿绫诲瀷锛� 0 绯荤粺鎴块棿  
    I_ROOM_TYPE_USER = 1
    #  鎴块棿绫诲瀷锛� 1 鐢ㄦ埛鎴块棿  

    I_ROOM_STATE_READY = 0
    #  鎴块棿鐘舵€�  0 鍑嗗鐘舵€� 
    I_ROOM_STATE_START = 1
    #  鎴块棿鐘舵€�  1 寮€濮嬬姸鎬侊紙娓告垙涓級
    I_ROOM_STATE_OVER = 2
    #  鎴块棿鐘舵€�  2 缁撴潫鐘舵€侊紙娓告垙缁撴潫锛� 
    I_ROOM_UP_LIMIT = 50
    #鎴块棿浜烘暟涓婇檺
    I_ROOM_LIST_NULL = 1041
    #鎴块棿鍒楄〃涓虹┖
    I_ROOM_LIST_OK = 1040
    #鍙栧緱鎴块棿鍒楄〃鎴愬姛
    I_ROOM_LIST_ERROR = 1042
    #鍙栧緱鎴块棿鍒楄〃澶辫触
    T_USER_INFO = "Sq_UserInfo"
    #  鐢ㄦ埛淇℃伅琛�

    T_USER_FRIENDS = "Sq_UserFriendsRelation"
    #    鐢ㄦ埛濂藉弸淇℃伅琛�

    T_MESSAGE = "Sq_message"
    #    娑堟伅淇℃伅琛�

    T_ROOMS = "Sq_room"
    #    鎴块棿淇℃伅琛�

    T_FEEDBACK = "Sq_Feedback"
    #    鍙嶉淇℃伅琛�

    T_IDIOM = "Sq_idiom"
    #    鎴愯淇℃伅琛�

    T_IDIOMLETTERS = "Sq_idiomletters"
#    鎴愯棣栧瓧淇℃伅琛�


    S_SEARCHFIELDS = "SearchFields";
    #sql涓鎼滅储瀛楁鐨勭殑key
    S_SEARCHCONDITION = "SearchCondition";
    #sql涓鎼滅储鏉′欢鐨刱ey
    S_RESULTROW = "resultRow";
    #sql涓鎼滅储缁撴灉鏉＄洰key
    S_TABLE = "table";
    #sql涓鎼滅储琛ㄧ殑key
    S_ORDERBY = "orderby"
    S_FETCH_ALL = "fetchAllData"
    #sql涓殑鎺掑簭瀛楁
    S_LIMIT = "limit"
    EARTH_RADIUS_METER = 6378137.0 
    #缁忕含搴﹀父閲�
    S_PINYIN_DB_FILE = "../data/Mandarin.dat"
    LOG_FILE_NAME="error.log"
    SYS_TRACE_INFO=1
    SYS_ERROR_COMMAND = "SYS#%s#%s"
    SYS_COMMAND_NOT_FOUND = 404
    SYS_CALL_COMMAND_ERROR = 500
    I_MAX_DISTANCE=1000
    I_MESSAGE_ADD_OK=4000
    I_FEEDBACK_ADD_OK=5000
    CommandMap = {
                "UL":"ULClass", #鐢ㄦ埛鐧诲綍
                "UR":"URClass", #鐢ㄦ埛娉ㄥ唽
                "PIS":"PISClass",
                "RI":"RIClass",
                "UPM":"UPMClass",
                "UIM":"UIMClass",
                "RU":"RUClass", #鎴块棿鐢ㄦ埛鍒楄〃
                "RGA":"RGAClass", #鐢ㄦ埛鍔犲叆鎴块棿
                "RISG":"RISGClass", #寮€濮嬫父鎴�
                "RIG":"RIGClass", #鎺ラ緳杩囩▼
                "RIC":"RICClass",#浣跨敤閬撳叿
                "RIFU":"RIFUClass",#閭€璇锋父鎴忕帺瀹跺垪琛�
                "RINU":"RINUClass",#闄勮繎鐜╁       
                "RIFA":"RIFAClass", #閭€璇风帺瀹�
                "RIFAC":"RIFACClass",#鍙嶉閭€璇�        
                "RIUE":"RIUEClass",#鐜╁鏀惧純娓告垙
                "RIKO":"RIKOClass",#鎴夸富韪汉
                "RISO":"RISOClass",#涓诲姩閫€鍑烘埧闂�
                "UFL":"UFLClass"#濂藉弸鍒楄〃
                
    }
#    鍛戒护绫诲搴斿叧绯�
    cfg = {
#           鏁版嵁搴撹繛鎺ラ厤缃�
           "DbConnectString" :{
                                                'user': 'root',
                                                'password': '123456',
                                                'host': '192.168.11.9',
                                                'database': 'sequence',
                                                'raise_on_warnings': True, },
    
    }
    
    ERROR_MESSAGE_ROOM_NULL = "鎴块棿瀛楀吀涓虹┖";
    #鎴块棿瀛楀吀涓虹┖
    ERROR_MESSAGE_ROOM_DETAIL_NULL = "鍦ㄦ埧闂村瓧鍏告棤娉曟壘鍒拌鎴块棿 ";
    #鎴块棿瀛楀吀涓虹┖
    ERROR_MESSAGE_USER_DETAIL_NULL = "鍦ㄧ敤鎴峰瓧鍏告棤娉曟壘鍒拌鐢ㄦ埛";
  
    
    ERROR_MESSAGE_ROOM_OWER_NULL = "鐢ㄦ埛闈炴鎴块棿鐨勬埧涓�";
    
    ERROR_MESSAGE_ROOM_USER_NO = "闈炴鎴块棿鐨勭敤鎴�";
    
    
    
    
    ROOM_MESSAGE_CODE_ADD_FILL = 2001;
    #鍔犲叆鎴块棿澶辫触
    ROOM_MESSAGE_CODE_ADD_SUSS = 2000;
    #鍔犲叆鎴块棿鎴愬姛
    ROOM_MESSAGE_CODE_UPPER_LIMIT = 2002;
    #杈惧埌涓婇檺浜烘暟
    
    ROOM_MESSAGE_CODE_START_LOWER_LIMIT = 2003;    
    #鏈揪鍒版父鎴忎汉鍛�
    ROOM_MESSAGE_CODE_START_SUSS = 2004;    
    #鏈揪鍒版父鎴忎汉鍛�
    
    
    ROOM_MESSAGE_CODE_IDIOM_SUSS = 2010;    
    #鎺ラ緳鎴愬姛    
    ROOM_MESSAGE_CODE_IDIOM_USED = 2011;    
    #宸蹭娇鐢ㄨ繃璇�
    ROOM_MESSAGE_CODE_IDIOM_NO = 2012;    
    #闈炴垚璇�
    ROOM_MESSAGE_CODE_IDIOM_FAIL = 2013;    
    #棣栧熬涓嶅

    
    
   

    
    EXIT_CMD = "EXIT";
    #socket鏂紑
    
    pinYin = None;
    #鎷奸煶瀵硅薄
    COMMENT_STYLE_HUSH=0;
    #鍢樹粬
    COMMENT_STYLE_UP=1;
    #鍔犳补
    COMMENT_STYLE_PRAISE=2;
    #璧�
    COMMENT_STYLE_QUICK=3;
    #蹇�
    



    


