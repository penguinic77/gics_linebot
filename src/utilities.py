import src.database as DB
from datetime import datetime

# 禮物資訊
def gift_info(score):
    gift=''
    if score == 100:
        gift = 'AIS3衣服+口罩+紀念磚+貼紙'
    elif score >= 85:
        gift = '口罩+紀念磚+貼紙'
    elif score >= 70:
        gift = '紀念磚+貼紙'
    elif score >= 30:
        gift = '貼紙'
    return gift


# 判斷字串是否存在括號{}且須合法並只存在一組
def is_str_close(a):
    lista = []
    flag = True
    num = 0
    if a.find("{") == -1 or a.find("}") == -1:
        return False
    for i in a:
        if num == 1:  # 若找到一組括號後還有字元則非法
            return False
        if i == "{":
            lista.append(i)
        elif i == "}":
            if len(lista) == 0 or lista.pop() != "{" or num > 1:
                return False
            else:
                num += 1
    if len(lista) != 0:
        flag = False
    return flag


# 檢查是否已完成所有題目
def check_completeall(user_id):
    data = DB.db_fecthuserinfo(user_id)

    if data['score'] == 100:
        return True
    else:
        return False
    
# 計算花費時間
def total_time(user_id):
    start_time_sql=f'SELECT start_time, end_time FROM `gics_users` WHERE `user_id` = \'{user_id}\''
    data = DB.db_execsqlall(start_time_sql)
    print("star_time:",data[0]['start_time'])
    start_time=data[0]['start_time']
    end_time=data[0]['end_time']
    #轉為list，並在插入小數點後，再轉回string，否則格式不對無法計算
    start=list(start_time)
    end=list(end_time)
    start.insert(10,".")
    end.insert(10,".")
    start_time = float("".join(start))
    end_time = float("".join(end))
    
    sdatetime = datetime.fromtimestamp(start_time)
    edatetime = datetime.fromtimestamp(end_time)
    time=round((edatetime-sdatetime).seconds/60,1)
    
    return time

# 計算排名
def Ranking(timestamp, user_id):
    # 將完成全部題目的時間加入資料庫
    endtime_sql = f'UPDATE `gics_users` SET `end_time` = \'{timestamp}\' WHERE `user_id` = \'{user_id}\''
    DB.db_execsql(endtime_sql)
    time=total_time(user_id)
    # 取得已完成的玩家數量
    sql = 'SELECT COUNT(*) FROM `gics_users` WHERE `score` = \'100\' AND `RANK` != \'0\''
    data = DB.db_execsqlall(sql)
    #print("已完成玩家數:",data[0]['COUNT(*)'])
    rank = data[0]['COUNT(*)']+1 # 自己的排名為完成的玩家數量再加1
    sql = f'UPDATE `gics_users` SET `RANK` = \'{rank}\' WHERE `user_id` = \'{user_id}\'' #更新自己的排名
    DB.db_execsql(sql)
    return rank, time


# 將字串分割排版，以'。'分割句字，並替換字串中的'\n'為真實的換行
def Strsplit(string):
    result = []
    result = string.split('。')
    for i in range(len(result)):
        result[i] = result[i].replace(r'\n', '\n')
    return result
