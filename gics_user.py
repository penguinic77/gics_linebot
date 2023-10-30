from functools import wraps
from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FollowEvent,
)
import re
import random
import time
import math
import json
import emoji
import src.api_request as api
import src.database as DB
import src.utilities as helper
import src.flexmsg as flex

app = Flask(__name__)

access_token = ''
channel_secret = ''

line_bot_api = LineBotApi(access_token)
handler = WebhookHandler(channel_secret)

# 題目編號列表
ques_number = ['5ELF', 'B0NS', 'AIS3', 'TEDS', 'TB0W',
               'TTGF', 'BA64', 'MSCD', 'BRA1', 'BXOW', 'D3MN', 'TR33']
regex = r"([0-9]{1,5})\^([0-9]{1,3}) MOD ([0-9]{1,5})"
# 禮物兌換列表
gift_list = []

@app.route("/", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)

    app.logger.info("Request body: " + body)
    json_data = json.loads(body)
    # print('json_data:', json_data)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)  # 如果傳送的是文字text
def text_message(event):
    text = event.message.text      # 取出文字
    reply_token = event.reply_token
    user_id = event.source.user_id
    timestamp = event.timestamp
    print('User ID: ', user_id, 'Message: ', event.message.text)
    if re.match('^2257$', text.lower()):
        api.reply_onemsg('嘿, 我是 2257', access_token,reply_token)
    elif text == '封印解除進度':  # 回傳目前已答對題目和分數
        data = DB.db_fecthuserinfo(user_id)
        currentnumber = ''
        solved = 0
        count=len(ques_number)
        for i in range(count):  # 計算答對了多少題
            if data[ques_number[i]] == 1:
                currentnumber += ques_number[i]+'\n'
                solved += 1
        flex.reply_progress_msg(data['score'],solved, access_token,reply_token)
    elif text == '教學':  # 回傳教學
        flex.reply_guide_msg(access_token,reply_token)
    elif text == '勇者想要寶藏':
        data = DB.db_fecthuserinfo(user_id)
        score = int(data['score'])
        if data['GIFT']:
            api.reply_onemsg("已經兌換過獎品囉~", access_token,reply_token)
        else:
            if score < 30:
                api.reply_onemsg(f"你的分數不足以兌換獎品呦~", access_token,reply_token)
                exit(0)
            else:
                gift=helper.gift_info(score)
            sql = f' SELECT * FROM `gics_users` WHERE `user_id` = \'{user_id}\' '
            data = DB.db_execsql(sql)
            if data['RANK'] :
                msg = ['你是第 '+str(data['RANK'])+' 位解開封印的勇者，你總共獲得了 ' +
                   str(data['score'])+' 分!']
            else:
                msg = ['你總共獲得了 ' +str(data['score'])+' 分!']
            msg.append('謝謝你的參與，請協助我們填寫問卷，讓我們知道有哪裡能夠改進!\n\n問卷連結：https://forms.gle/4mETcwdLQe2rtDLB8')
            msg.append('你可以獲得以下寶藏：\n\n'+gift)
            question = ('是否要兌換?')
            gift_list.append(user_id)
            api.reply_confirm_template(msg, question, access_token, reply_token)

    elif gift_list and user_id in gift_list:
        if text.lower() == 'yes':
            sql = f' UPDATE `gics_users` SET `GIFT` = \'1\' WHERE `user_id` = \'{user_id}\''
            DB.db_execsql(sql)
            msg = '確認兌換'
            gift_list.remove(f'{user_id}')
            api.reply_onemsg(msg,access_token,reply_token)
        else:
            msg = '取消兌換'
            gift_list.remove(f'{user_id}')
            api.reply_onemsg(msg,access_token,reply_token)
    elif text == '封印位置':  # 回傳隨機提示
        num = random.randrange(200) % 11 + 1  # 產生隨機1~11的數字
        sql = f' SELECT * FROM `gics_numtip` WHERE `num` = \'{num}\''
        data = DB.db_execsql(sql)
        flex.reply_tip(data['tip'],access_token,reply_token)
    elif re.search('-提示', text.upper()):      # 如果是-提示相關的文字
        sql = ' SELECT * FROM `gics_exam` WHERE `number` = \'' + text.upper() + '\''
        sql = re.sub(r"-提示(\w?)", "", sql)
        # 取得hint的number,有些題目會有多個提示
        pattern = re.compile(r"-提示(.?)", re.S)
        hint_num = re.findall(pattern, text.upper())
        data = DB.db_execsql(sql)
        if data is None:
            api.reply_onemsg('題號不正確哦 更改一下再試試吧~',
                             access_token,reply_token)
        else:
            x = 'hint'+str(hint_num[0])
            hint = data[x].replace('。', '\n')  # 產生換行
            if data['hint_img'] != '':
                api.reply_oneimgmsg(hint, data['hint_img'], access_token,reply_token)
            else:
                api.reply_onemsg(hint, access_token,reply_token)
    elif re.search('-故事', text.upper()):
        sql = ' SELECT story FROM `gics_exam` WHERE `number` = \'' + text.upper() + '\''
        sql = re.sub(r"-故事(\w?)", "", sql)
        data=DB.db_execsql(sql)
        if data is None:
            api.reply_onemsg('故事題號不正確哦 更改一下再試試吧~',
                             access_token,reply_token)
        else:
            story=helper.Strsplit(data['story'])
            flex.reply_story(story[0],access_token,reply_token)
                 
    elif re.search('-', text):  # 如果是-答案相關的文字
        number = re.sub(r'-.*', "", text)
        data = DB.db_fecthexaminfo(number,'*')
        if data is None:
            api.reply_onemsg('題號不正確哦 更改一下再試試吧~',
                             access_token,reply_token)
        else:
            if text.find('-') != -1:
                answer = text.split('-')[1]
            else:
                answer = ''
            if data['answer'] == answer:  # 如果答案正確
                score = data['score']  # 該題的可得分數
                # 判斷是否已經答對此題目
                if DB.add_score(timestamp, user_id, number, score) == False:    # 第一次答對
                    userinfo = DB.db_fecthuserinfo(user_id)
                    accumscore = userinfo['score']  # 累積分數
                    reply_right = f'回答正確!恭喜獲得{score}分!現在累計{accumscore}分!'
                    reply_list = [reply_right]
                    story = helper.Strsplit(data['story'])  # 該題的故事
                    #story_list = helper.Strsplit(story) #注意這邊的List最多為4筆，否則會超出reply限制
                    #reply_arr.extend(story_list)
                    completeall = helper.check_completeall(user_id)
                    print("是否通關:", completeall)
                    # 檢查是否已完成所有題目
                    if completeall == False:
                        flex.reply_story(story[0],access_token,reply_token,reply_list)
                    else:
                        myrank,time = helper.Ranking(timestamp, user_id)
                        reply_list.append(
                            f'封印已經全部解開了，感謝勇者大人，你是第{myrank}名!!!\n總共花了{time}分鐘\n\n請勇者大人回到 AIS3 的攤位吧，我已經準備好獎勵等著你了>w<')
                        flex.reply_story(story[0],access_token,reply_token,reply_list)
                else:   # 已經答對
                    api.reply_onemsg('你已經答對這題囉~挑戰其他題目試試看!',access_token,reply_token)
            else:  # 題目答錯
                api.reply_onemsg(data['reply_wrong'],
                                 access_token,reply_token)
    elif text == '精靈幫幫我': # 客服功能
        msg = '勇者大人很抱歉現在我魔力消耗過大(´;ω;`)，沒辦法幫上你，但別擔心我會呼叫其他小精靈來協助你解決問題~'
        user_name=api.fetch_username(user_id,access_token)
        api.reply_onemsg(msg,access_token,reply_token)
        notice=f'勇者：\"{user_name}\" 需要您的協助~'
        api.line_notify_to_GM(notice)
    elif re.search(regex, text.upper(), re.DOTALL):
        matches = re.search(regex, text.upper(), re.DOTALL)
        ans = int(math.pow(int(matches.group(1)), int(
            matches.group(2))) % int(matches.group(3)))
        api.reply_onemsg(f'答案:{ans}', access_token,reply_token)

    else: 
        data = DB.db_fecthexaminfo(text.upper(),'*')
        if data is not None:      
            string = data['question']
            question = helper.Strsplit(string)
            if data['question_img'] != '':
                api.reply_imgmsg(
                    question, data['question_img'], access_token,reply_token)
            else:
                api.reply_multimsg(question, access_token,reply_token)
            
            
@handler.add(FollowEvent)  # 加好友事件
def follow_message(event):
    timestamp=event.timestamp
    reply_token = event.reply_token
    user_id = event.source.user_id
    user_name=api.fetch_username(user_id,access_token)
    
    DB.db_checkuserid(timestamp, user_id ,user_name)  # 檢查userid是否有存在資料庫，若沒有則新增
    flex.reply_welcome_msg(access_token,reply_token)
    #msg_greet = '歡迎你，勇者大人，我已經等你很久了。\n\n我是上古時期被魔王封印在此處的女婕思精靈。\n數萬年來，我一直在找尋像你這樣具有資安能力的勇者。\n\n魔王在此地設下了許多封印的結界，需要你的幫忙才可以解除。\n\n如果你願意幫助我解開封印，我會將寶藏送給你，拜託了，勇者大人。'
    #msg_guide = '請勇者大人點擊使用教學，或輸入\"教學\"來查看說明呦~'
    #reply_arr = [msg_greet, msg_guide]
    #api.reply_multimsg(reply_arr, access_token,reply_token)


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000, threads=8)
