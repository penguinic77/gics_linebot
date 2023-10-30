import src.api_request as api


# 回傳歡迎訊息(flex)
def reply_welcome_msg(actok, rk):
    contents={
      "type": "bubble",
      "header": {
        "type": "box",
        "layout": "baseline",
        "contents": [
          {
            "type": "icon",
            "url": "https://i.imgur.com/vA4f3t7.png",
            "size": "xxl",
            "offsetStart": "xxl"
          },
          {
            "type": "text",
            "text": "歡迎你，勇者大人~",
            "weight": "bold",
            "size": "xl",
            "align": "center"
          },
          {
            "type": "icon",
            "url": "https://i.imgur.com/vA4f3t7.png",
            "size": "xxl",
            "offsetEnd": "xl"
          }
        ],
        "paddingAll": "md"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "icon",
                "url": "https://i.imgur.com/fJGov4F.png",
                "size": "3xl",
                "offsetStart": "xs"
              },
              {
                "type": "text",
                "wrap": True,
                "weight": "bold",
                "size": "md",
                "text": "我已經等你很久了~\n我是上古時期被魔王封印在此處的女婕思精靈\n\n數萬年來，我一直在找尋像你這樣具有資安能力的勇者 \n\n魔王在此地設下了許多封印的結界，需要你的幫忙才可以解除",
                "offsetBottom": "lg"
              }
            ],
            "paddingAll": "md"
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "icon",
                "url": "https://i.imgur.com/g0iNczp.png",
                "size": "xxl"
              },
              {
                "type": "text",
                "text": "如果你願意幫助我解開封印，我會將寶藏送給你，拜託了，勇者大人",
                "wrap": True,
                "weight": "bold",
                "offsetBottom": "lg"
              }
            ],
            "paddingAll": "xl"
          }
        ],
        "paddingAll": "xs"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "點我查看教學",
              "text": "教學"
            },
            "flex": 2,
            "style": "secondary"
          }
        ]
      },
      "styles": {
        "header": {
          "backgroundColor": "#f8ad9d"
        },
        "hero": {
          "backgroundColor": "#e6ccb2"
        },
        "body": {
          "backgroundColor": "#ffdab9"
        }
      }
    }
    api.reply_flexmsg(contents, actok, rk)



# 回傳教學訊息(flex)
def reply_guide_msg(actok, rk):
    contents={
      "type": "bubble",
      "header": {
        "type": "box",
        "layout": "baseline",
        "contents": [
          {
            "type": "icon",
            "url": "https://i.imgur.com/MDUv4pB.png",
            "size": "3xl",
            "offsetStart": "xxl"
          },
          {
            "type": "text",
            "text": "遊戲方式",
            "weight": "bold",
            "size": "xl",
            "align": "center"
          },
          {
            "type": "icon",
            "url": "https://i.imgur.com/MDUv4pB.png",
            "size": "3xl",
            "offsetEnd": "xxl"
          }
        ],
        "paddingAll": "md"
      },
      "hero": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "1. ",
                "size": "sm",
                "flex": 0,
                "weight": "bold",
                "margin": "none"
              },
              {
                "type": "text",
                "text": "在女婕思會場中，有許多右下角貼有AIS3貼紙的封印咒語",
                "size": "sm",
                "flex": 0,
                "weight": "bold",
                "wrap": True
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "2. ",
                "size": "sm",
                "weight": "bold",
                "flex": 0
              },
              {
                "type": "text",
                "text": "輸入封印咒語，精靈就會分析並將封印的題目告訴勇者",
                "wrap": True,
                "weight": "bold",
                "size": "sm"
              }
            ],
            "paddingTop": "xs"
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "3. ",
                "size": "sm",
                "weight": "bold",
                "flex": 0
              },
              {
                "type": "text",
                "text": "將正確答案告訴精靈就能解除封印（格式要正確），以此獲得分數來兌換女婕思精靈的寶藏",
                "wrap": True,
                "weight": "bold",
                "size": "sm"
              }
            ],
            "paddingTop": "sm"
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "4. ",
                "size": "sm",
                "weight": "bold",
                "flex": 0
              },
              {
                "type": "text",
                "text": "若是有遊戲方式的疑問，可以使用\"精靈幫幫我\"，會有專門的小精靈來幫助你～",
                "wrap": True,
                "weight": "bold",
                "size": "sm"
              }
            ],
            "paddingTop": "sm"
          }
        ],
        "paddingAll": "xl"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "勇者請查看！",
            "weight": "bold",
            "size": "xl",
            "align": "center"
          },
          {
            "type": "text",
            "text": "（精靈對話範例）",
            "weight": "bold",
            "size": "xl",
            "align": "center"
          },
          {
            "type": "image",
            "url": "https://i.imgur.com/k5fjAbn.jpg",
            "size": "full",
            "aspectRatio": "1170:2038"
          }
        ]
      },
      "styles": {
        "header": {
          "backgroundColor": "#ddb892"
        },
        "hero": {
          "backgroundColor": "#e6ccb2"
        },
        "body": {
          "backgroundColor": "#ede0d4"
        }
      }
    }
    api.reply_flexmsg(contents, actok, rk)


# 回傳解題進度訊息(flex)
def reply_progress_msg(score, solved, actok, rk):
    gift=[]
    # 魔法陣 
    magic_circle=["https://i.imgur.com/BOhbzL9.png",
                  "https://i.imgur.com/F4dF5AP.png","https://i.imgur.com/F2BkcEa.png",
                  "https://i.imgur.com/5TcIibJ.png","https://i.imgur.com/BCNCOLA.png",
                  "https://i.imgur.com/FoG5oI3.png","https://i.imgur.com/wQeU4ZT.png",
                  "https://i.imgur.com/HN2TgXa.png","https://i.imgur.com/iG9GhAb.png",
                  "https://i.imgur.com/cHevxfx.png","https://i.imgur.com/mWXOC7l.png",
                  "https://i.imgur.com/TU1aVkV.png","https://i.imgur.com/2zdw8Kq.png"
    ]
    #根據以解出的題數顯示魔法陣的解除情況
    mcircle_images=magic_circle[solved]
    
    # 禮物資訊
    if score < 30:
        gift.extend([
            {
              "type": "text",
              "text": "努力解除封印來獲得寶藏吧~",
              "weight": "bold"
            }])
    if score >= 30:
        gift.extend([{
              "type": "icon",
              "url": "https://i.imgur.com/G9qxUGO.png",
            },
            {
              "type": "text",
              "text": "貼紙",
              "weight": "bold"
            }])
    if score >= 70:
        gift.extend([
            {
              "type": "icon",
              "url": "https://i.imgur.com/NDoTf0o.png",
              "offsetEnd": "md"
            },
            {
              "type": "text",
              "text": "紀念磚",
              "weight": "bold",
              "offsetEnd": "md"
            }
            ])
    if score >= 85:
        gift.extend([
            {
            "type": "icon",
            "url": "https://i.imgur.com/wgeRRxo.png",
            "offsetEnd": "sm"
            },
            {
              "type": "text",
              "text": "口罩",
              "weight": "bold",
              "offsetEnd": "sm"
            }
            ])
    if score == 100:
        gift.extend([{
              "type": "icon",
              "url": "https://i.imgur.com/qoNA3FX.png",
              "offsetEnd": "sm"
            },
            {
              "type": "text",
              "text": "衣服",
              "align": "start",
              "size": "md",
              "offsetEnd": "sm",
              "weight": "bold",
            }])
    
    # flex內容
    contents={
    "type": "bubble",
    "header": {
      "type": "box",
      "layout": "baseline",
      "contents": [
        {
          "type": "icon",
          "size": "3xl",
          "offsetStart": "xxl",
          "url": "https://i.imgur.com/RmpQ3T2.png"
        },
        {
          "type": "text",
          "text": "封印解除進度",
          "weight": "bold",
          "align": "center",
          "size": "xl"
        },
        {
          "type": "icon",
          "size": "3xl",
          "url": "https://i.imgur.com/RmpQ3T2.png",
          "offsetEnd": "xxl"
        }
      ],
      "paddingAll": "md"
    },
    "hero": {
      "type": "image",
      "url": f"{mcircle_images}",
      "size": "full",
      "aspectMode": "cover",
      "aspectRatio": "20:18"
    },
    "body": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "box",
              "layout": "baseline",
              "contents": [
                {
                  "type": "icon",
                  "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                },
                {
                  "type": "text",
                  "text": "分數",
                  "size": "lg",
                  "weight": "bold"
                },
                {
                  "type": "text",
                  "text": f"{score}",
                  "size": "lg",
                  "color": "#111111",
                  "align": "end",
                  "weight": "bold"
                }
              ]
            },
            {
              "type": "box",
              "layout": "baseline",
              "contents": [
                {
                  "type": "icon",
                  "url": "https://i.imgur.com/6SmR5aa.png"
                },
                {
                  "type": "text",
                  "text": "已解除封印數",
                  "size": "lg",
                  "color": "#555555",
                  "weight": "bold"
                },
                {
                  "type": "text",
                  "text": f"{solved}",
                  "size": "lg",
                  "color": "#111111",
                  "align": "end",
                  "weight": "bold"
                }
              ]
            },
            {
              "type": "separator",
              "color": "#6c757d",
              "margin": "none"
            }
          ],
          "offsetBottom": "sm"
        },
        {
          "type": "box",
          "layout": "baseline",
          "contents": [
            {
              "type": "icon",
              "url": "https://i.imgur.com/g0iNczp.png"
            },
            {
              "type": "text",
              "text": "可獲得寶藏：",
              "size": "lg",
              "weight": "bold",
              "offsetTop": "xs"
            }
          ],
          "borderWidth": "none",
          "borderColor": "#495057",
          "offsetTop": "sm"
        },
        {
          "type": "box",
          "layout": "baseline",
          "contents": gift,
          "borderWidth": "none",
          "cornerRadius": "none",
          "offsetTop": "none",
          "paddingTop": "md"
        }
      ],
      "backgroundColor": "#BBD0FF"
    },
    "styles": {
      "header": {
        "backgroundColor": "#C8B6FF"
      },
      "hero": {
        "backgroundColor": "#B8C0FF"
      }
    }
    }
    api.reply_flexmsg(contents, actok, rk)
    
# 回傳提示訊息
def reply_tip(tip, actok, rk):
    contents={
    "type": "bubble",
    "header": {
      "type": "box",
      "layout": "baseline",
      "contents": [
        {
          "type": "icon",
          "url": "https://i.imgur.com/xNJUo0H.png",
          "size": "xxl",
          "offsetStart": "xxl"
        },
        {
          "type": "text",
          "text": "精靈感知",
          "weight": "bold",
          "size": "xl",
          "align": "center"
        },
        {
          "type": "icon",
          "url": "https://i.imgur.com/xNJUo0H.png",
          "size": "xxl",
          "offsetEnd": "xxl"
        }
      ],
      "paddingAll": "md"
    },
    "body": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "text",
          "wrap": True,
          "weight": "bold",
          "size": "md",
          "text": f"{tip}",
          "align": "center"
        },
        {
          "type": "text",
          "text": "勇者大人，我們去看看吧!",
          "weight": "bold",
          "size": "md",
          "align": "center",
          "offsetTop": "md"
        }
      ],
      "paddingTop": "sm"
    },
    "styles": {
      "header": {
        "backgroundColor": "#e7c6ff"
      },
      "hero": {
        "backgroundColor": "#e6ccb2"
      },
      "body": {
        "backgroundColor": "#ffe5ec"
      }
    }
    }
    api.reply_flexmsg(contents, actok, rk)

#回傳故事訊息(flex)
def reply_story(story, actok, rk, msg_list=[]):
  contents ={
  "type": "bubble",
  "header": {
    "type": "box",
    "layout": "baseline",
    "contents": [
      {
        "type": "icon",
        "url": "https://i.imgur.com/x3tMKah.png",
        "size": "xxl",
        "offsetStart": "xxl",
        "margin": "xxl"
      },
      {
        "type": "text",
        "text": "女婕思歷史殘片",
        "weight": "bold",
        "size": "lg",
        "align": "center"
      },
      {
        "type": "icon",
        "url": "https://i.imgur.com/x3tMKah.png",
        "size": "xxl",
        "offsetEnd": "xxl",
        "margin": "xs"
      }
    ],
    "paddingAll": "xs"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": f"{story}",
        "wrap": True,
        "weight": "bold"
      }
    ]
  },
  "styles": {
    "header": {
      "backgroundColor": "#8d99ae"
    },
    "body": {
      "backgroundColor": "#edf2f4"
    }
  }
  }
  if len(msg_list)==0:
    api.reply_flexmsg(contents, actok, rk)
  else:
    api.reply_textflex(msg_list,contents, actok, rk)
  

# 回傳表格訊息(flex)
def reply_separator_msg(temp_dict, actok, rk):
    contents = [{
        "type": "separator",
                "color": "#000000"
    }]
    for i in temp_dict:
        contents.append(
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                        {
                            "type": "text",
                            "text": i,
                            "offsetStart": "5px"
                        },
                    {
                            "type": "separator",
                            "color": "#000000"
                            },
                    {
                            "type": "text",
                            "text": temp_dict[i],
                            "offsetStart": "5px"
                            }
                ]
            }
        )
        contents.append(
            {
                "type": "separator",
                "color": "#000000"
            }
        )
        
    
    
    contents={
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": contents
                    }
                }
    api.reply_flexmsg(contents, actok, rk)
    
    #headers = {'Authorization': f'Bearer {actok}',
    #           'Content-Type': 'application/json'}
    #body = {
    #    'replyToken': rk,
    #    'messages': [
    #        {
    #            "type": "flex",
    #            "altText": "Flex Message",
    #            "contents": contents
    #        }
    #    ]
    #}
    #req = requests.request('POST', 'https://api.line.me/v2/bot/message/reply',
    #                       headers=headers, data=json.dumps(body).encode('utf-8'))
    #print(req.text)
