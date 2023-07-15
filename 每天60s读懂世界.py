# @author Sten
# 作者仓库:https://github.com/aefa6/QinglongScript.git
# 觉得不错麻烦点个star谢谢

import requests
import json

# Sever酱推送接口
sc_key = '这里填Sever酱的push key' 
# 下面的不用管了
sc_url = f'https://sc.ftqq.com/{sc_key}.send'
url = 'https://60s.viki.moe/?encoding=text'  # 来自知乎的一位大佬的接口
resp = requests.get(url)
news = resp.text.replace('\n', '\n      \n    ')

info = f"""
{news}   
"""

# Sever酱推送
requests.post(sc_url, data={'text': '60s读懂世界', 'desp': info})
