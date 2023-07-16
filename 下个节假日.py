# @author Sten
# 作者仓库:https://github.com/aefa6/QinglongScript.git
# 觉得不错麻烦点个star谢谢

import requests
import json
import notify

title = "下个节假日" 

dateurl = 'https://date.appworlds.cn/next'
date1url = 'https://date.appworlds.cn/next/days'
holiday = requests.get(dateurl)
holiday1 = requests.get(date1url)

desc = json.loads(holiday.text)
desc1 = json.loads(holiday1.text)

daytime = desc['data']['date']
dayname = desc['data']['name']
Remain = desc1['data']

info = f"""
下个节假日是{Remain}天后的{dayname}（{daytime}）
"""
print(info)
notify.send(title, info)
