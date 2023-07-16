# @author Sten
# 作者仓库:https://github.com/aefa6/QinglongScript.git
# 觉得不错麻烦点个star谢谢
# 使用青龙自带的通知
import requests
import json
import notify
url = 'https://60s.viki.moe/?encoding=text'  # 来自知乎的一位大佬的接口
resp = requests.get(url)
news = resp.text.replace('\n', '\n      \n    ')

info = f"""
{news}   
"""

notify.send("每天60s读懂世界", info)
