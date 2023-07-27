# @author Sten
# 作者仓库:https://github.com/aefa6/QinglongScript.git
# 觉得不错麻烦点个star谢谢
# 使用青龙自带的通知
import requests
import json
import notify

url = 'https://60s.viki.moe/?encoding=text'
resp = requests.get(url)

# 分片处理
pieces = resp.text.split('\n', 8)
content1 = '\n'.join(pieces[:8])  
content2 = '\n'.join(pieces[8:])

info1 = f"""
{content1}   
"""
info2 = f"""
{content2}   
"""

# 发送分片推送  
notify.send("每天60s读懂世界", info1 + "\n\n")
notify.send("每天60s读懂世界", info2)
