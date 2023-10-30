import pymysql.cursors  # 載入 pymysql 模組，處理python和mysql的連結

# 連接資料庫的資訊
db_info = pymysql.Connect(
    host='127.0.0.1',
    user='root',
    password='4ycxzE3obE',
    db='gics_DB',
    cursorclass=pymysql.cursors.DictCursor)


# 執行sql操作(取一筆)
def db_execsql(sql):
    result = ''
    try:
        db_conn = db_info
        db_conn.ping(reconnect=True)
        with db_conn.cursor() as cur:
            cur.execute(sql)
            result = cur.fetchone()  # 最多一筆
        db_conn.commit()
        return result

    except Exception as e:
        return e


# 執行sql操作(取全部)
def db_execsqlall(sql):
    result = ''
    try:
        db_conn = db_info
        db_conn.ping(reconnect=True)
        with db_conn.cursor() as cur:
            cur.execute(sql)
            result = cur.fetchall()  # 取全部
        db_conn.commit()
        return result

    except Exception as e:
        return e


# 增加userid和起始時間進資料庫
def add_userinfo(timestamp, user_id ,user_name):
    sql = f"INSERT INTO `gics_users` (`user_id`, `user_name`, `start_time`) VALUES ('{user_id}','{user_name}','{timestamp}')"
    db_execsql(sql)


# 增加user的分數
def add_score(timestamp, user_id, number, score):
    number=number.upper()
    num_sql = f' SELECT * FROM `gics_users` WHERE `user_id` = \'{user_id}\''
    data = db_execsql(num_sql)
    if data[f'{number}'] == 0:
        num_sql = f' UPDATE `gics_users` SET `{number}` = \'1\' WHERE `user_id` = \'{user_id}\''
        sumscore = score + data['score']  # 加總分數
        sumscore_sql = f' UPDATE `gics_users` SET `score` = \'{sumscore}\' WHERE `user_id` = \'{user_id}\''
        ans_sql = f"INSERT INTO `gics_anslog` (`timestamp`, `user_id`, `number`) VALUES ('{timestamp}','{user_id}','{number}')"
        # 將第一次答對的資訊存入資料庫
        try:
            db_conn = db_info
            db_conn.ping(reconnect=True)
            with db_conn.cursor() as cur:
                cur.execute(sumscore_sql)
                cur.execute(num_sql)
                cur.execute(ans_sql)
            db_conn.commit()

        except Exception as e:
            return e
        return False  # 尚未答對過此題
    else:
        return True  # 已答對過此題


# 取得題目資料
def db_fecthexaminfo(number,column):
    data = []
    sql = f' SELECT {column} FROM `gics_exam` WHERE `number` = \'' + number+'\''
    data = db_execsql(sql)
    return data


# 取得使用者資料
def db_fecthuserinfo(user_id):
    data = []
    sql = ' SELECT * FROM `gics_users` WHERE `user_id` = \'' + user_id + '\''
    data = db_execsql(sql)
    return data


# 檢查使用者ID是否存在資料庫
def db_checkuserid(timestamp, user_id, user_name):
    sql = ' SELECT * FROM `gics_users` WHERE `user_id` = \'' + user_id + '\''
    data = db_execsql(sql)
    if data is None:
        add_userinfo(timestamp, user_id, user_name)
        print("新使用者: ",user_id,"暱稱: ",user_name)
        return False
    else:
        return True

# 取得題目的故事
def db_story(number):
    story_result = []
    data = db_fecthexaminfo(number)
    story = data['story']
    story = '-----小故事-----\n' + story + '\n-------------'
    story_result = story.split('。')
    return story_result
