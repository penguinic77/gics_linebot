import requests
import json
from linebot import LineBotApi, WebhookHandler

# 官方API文件: https://developers.line.biz/en/reference/messaging-api/#rich-menu
# 請填入正確的access_token
access_token = ''
line_bot_api = LineBotApi(access_token)
headers = {'Authorization': f'Bearer {access_token}',
           'Content-Type': 'application/json'}
################################################################################
# 建立一個richmenu，填入想要設計的格式大小
# 以下為richmenu建立的格式

body = {
    "size": {
        "width": 800,
        "height": 270
    },
    "selected": 'true',
    "name": "Gics Rich menu ",
    "chatBarText": "點下去有好用的功能呦~",
    "areas": [
        {
            "bounds": {
                "x": 0,
                "y": 0,
                "width": 266,
                "height": 270
            },
            "action": {
                "type": "message",
                        "label": "使用教學",
                "text": "教學"
            }
        },
        {
            "bounds": {
                "x": 266,
                "y": 0,
                "width": 267,
                "height": 270
            },
            "action": {
                "type": "message",
                        "label": "進度",
                "text": "封印解除進度"
            }
        },
        {
            "bounds": {
                "x": 533,
                "y": 0,
                "width": 266,
                "height": 270
            },
            "action": {
                "type": "message",
                        "label": "小提示",
                "text": "封印位置"
            }
        }
    ]
}
req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu',
                       headers=headers, data=json.dumps(body).encode('utf-8'))

rhmu_str=req.text 
rhmu_dict=eval(rhmu_str) # 轉換string為dict
rhmuid=rhmu_dict['richMenuId'] #取得richmenu的ID
print(rhmuid)


# 請填入圖片檔名的路徑
# 注意!圖片大小務必為800x270(或是你上一步設定的大小)，不然這邊會報錯
menu_path = '/root/gics/richmenu/menu_2023.jpg'
with open(f'{menu_path}', 'rb') as f:
    line_bot_api.set_rich_menu_image(
        f'{rhmuid}', 'image/jpeg', f)

# 啟用richmenu 
req = requests.request(
    'POST', f'https://api.line.me/v2/bot/user/all/richmenu/{rhmuid}', headers=headers)
print("done")

################################################################################
# 使用時請將上方header之後的部分都註解，以免造成錯誤
# 取得目前的richmenu列表
'''
req = requests.request('GET', 'https://api.line.me/v2/bot/richmenu/list',
                       headers=headers)
print(req.text)
'''
################################################################################
# 刪除指定的richmenu (ID記得要改)
'''
line_bot_api.delete_rich_menu(
    'richmenu-36d46bda06bac7e0acaa6d957e6f0724')
'''
################################################################################
