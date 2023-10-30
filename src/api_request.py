import requests
import json
import re


# 取得使用者名稱
def fetch_username(userid,actok):
    headers = {'Authorization': f'Bearer {actok}'}
    req = requests.request('GET', f'https://api.line.me/v2/bot/profile/{userid}',
                           headers=headers)
    usr_profile=eval(req.text)
    user_name=re.sub(r'[^\w\s]', '', usr_profile['displayName']) #去除名子中的特殊符號，但保留空格
    return user_name 


# LINE Push 一則訊息到 GM 
def line_notify_to_GM(msg):
    ACCESS_TOKEN = ""
    headers = {'Authorization': f'Bearer {ACCESS_TOKEN}'}
    body = {
        'message': msg
    }
    req = requests.request('POST', 'https://notify-api.line.me/api/notify',
                           headers=headers, data=body)
    print(req.text)


# LINE 回傳一則訊息函式
def reply_onemsg(msg, actok, rk):
    headers = {'Authorization': f'Bearer {actok}',
               'Content-Type': 'application/json'}
    body = {
        'replyToken': rk,
        'messages': [{
            "type": "text",
            "text": msg
        }]
    }
    req = requests.request('POST', 'https://api.line.me/v2/bot/message/reply',
                           headers=headers, data=json.dumps(body).encode('utf-8'))
    print(req.text)

# LINE 回傳多則傳訊息函式(Line限制一次最多五則)
def reply_multimsg(msg, actok, rk):
    messagelist = [{
        "type": "text",
        "text": msg[0]
    }]
    for i in range(1, len(msg)):  # 判斷有幾則訊息並加入mseeagelist
        messagelist.append({
            "type": "text",
            "text": msg[i]
        })

    headers = {'Authorization': f'Bearer {actok}',
               'Content-Type': 'application/json'}
    body = {
        'replyToken': rk,
        'messages': messagelist
    }
    req = requests.request('POST', 'https://api.line.me/v2/bot/message/reply',
                           headers=headers, data=json.dumps(body).encode('utf-8'))
    print(req.text)


# LINE 主動發出訊息函式(免費用戶計畫限制每月最多500則，所以盡量少用)
def push_msg(msg, actok, bnpcid):
    headers = {'Authorization': f'Bearer {actok}',
               'Content-Type': 'application/json'}
    body = {
        'to': bnpcid,
        'messages': [{
            'type': 'text',
            'text': msg
        }]
    }
    req = requests.request('POST', 'https://api.line.me/v2/bot/message/push',
                           headers=headers, data=json.dumps(body).encode('utf-8'))
    print(req.text)


# LINE 主動向所有為好友的用戶發出訊息函式
def push_broadcast(msg, actok):
    headers = {'Authorization': f'Bearer {actok}',
               'Content-Type': 'application/json'}
    body = {
        'messages': [{
            "type": "text",
            "text": msg
        }]
    }
    req = requests.request('POST', 'https://api.line.me/v2/bot/message/broadcast',
                           headers=headers, data=json.dumps(body).encode('utf-8'))
    print(req.text)


# LINE 回傳圖片函式
def reply_image(msg, actok, rk):
    headers = {'Authorization': f'Bearer {actok}',
               'Content-Type': 'application/json'}
    body = {
        'replyToken': rk,
        'messages': [{
            'type': 'image',
            'originalContentUrl': msg,
            'previewImageUrl': msg
        }]
    }
    req = requests.request('POST', 'https://api.line.me/v2/bot/message/reply',
                           headers=headers, data=json.dumps(body).encode('utf-8'))
    print(req.text)


def reply_oneimgmsg(msg, image, actok, rk):
    headers = {'Authorization': f'Bearer {actok}',
               'Content-Type': 'application/json'}
    body = {
        'replyToken': rk,
        'messages': [{
            "type": "text",
            "text": msg
        }, {
            "type": "image",
            'originalContentUrl': image,
            'previewImageUrl': image}]
    }
    req = requests.request('POST', 'https://api.line.me/v2/bot/message/reply',
                           headers=headers, data=json.dumps(body).encode('utf-8'))
    print(req.text)

# 回傳圖文訊息(圖為最後一則訊息)
def reply_imgmsg(msg, image, actok, rk):
    messagelist = [{
        "type": "text",
        "text": msg[0]
    }]
    for i in range(1, len(msg)):  # 判斷有幾則訊息並加入mseeagelist
        messagelist.append({
            "type": "text",
            "text": msg[i]
        })
    messagelist.append({
        "type": "image",
        'originalContentUrl': image,
        'previewImageUrl': image})

    headers = {'Authorization': f'Bearer {actok}',
               'Content-Type': 'application/json'}
    body = {
        'replyToken': rk,
        'messages': messagelist
    }
    req = requests.request('POST', 'https://api.line.me/v2/bot/message/reply',
                           headers=headers, data=json.dumps(body).encode('utf-8'))
    print(req.text)

def reply_confirm_template(msg, question, actok, rk):
    messagelist = [{
        "type": "text",
        "text": msg[0]
    }]

    for i in range(1, len(msg)):  # 判斷有幾則訊息並加入mseeagelist
        messagelist.append({
            "type": "text",
            "text": msg[i]
        })

    messagelist.append({
        "type": "template",
        "altText": 'msg',
        "template": {
            "type": "confirm",
            "text": question,
            "actions": [
                {
                    "type": "message",
                    "label": "Yes",
                    "text": "yes"
                },
                {
                    "type": "message",
                    "label": "No",
                    "text": "no"
                }
            ]
        }
    })

    headers = {'Authorization': f'Bearer {actok}',
               'Content-Type': 'application/json'}
    body = {
        'replyToken': rk,
        'messages': messagelist
    }
    req = requests.request('POST', 'https://api.line.me/v2/bot/message/reply',
                           headers=headers, data=json.dumps(body).encode('utf-8'))

# 回傳flex訊息
def reply_flexmsg(contents, actok, rk):
    headers = {'Authorization': f'Bearer {actok}',
               'Content-Type': 'application/json'}
    body = {
        'replyToken': rk,
        'messages': [
            {
            "type": "flex",
            "altText": "Flex Message",
            "contents": contents
            }
        ]
    } 
    req = requests.request('POST', 'https://api.line.me/v2/bot/message/reply',
                           headers=headers, data=json.dumps(body).encode('utf-8'))
    print(req.text)

def reply_textflex(msg, contents, actok, rk):
    messagelist = [{
        "type": "text",
        "text": msg[0]
    }]
    for i in range(1, len(msg)):  # 判斷有幾則訊息並加入mseeagelist
        messagelist.append({
            "type": "text",
            "text": msg[i]
        })
    
    messagelist.append({
                "type": "flex",
                "altText": "Flex Message",
                "contents": contents
            })
    headers = {'Authorization': f'Bearer {actok}',
               'Content-Type': 'application/json'}
    body = {
        'replyToken': rk,
        'messages': messagelist
    }
    
    #print(json.dumps(body).encode('utf-8'))
    req = requests.request('POST', 'https://api.line.me/v2/bot/message/reply',
                           headers=headers, data=json.dumps(body).encode('utf-8'))
    print(req.text)