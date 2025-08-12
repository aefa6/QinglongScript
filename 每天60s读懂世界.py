# @author Sten
# 作者仓库:https://github.com/aefa6/QinglongScript.git
# 觉得不错麻烦点个star谢谢
# 使用青龙自带的通知，某些推送不支持较长的文本推送，故默认分片推送，如果需要合并推送请将25和26行加#注释掉，29行去除#注释即可。
import requests
import json
import notify

url = 'https://60s.viki.moe/v2/60s?encoding=text'
resp = requests.get(url)
content = resp.text
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

# 全文整段发送推送  
# notify.send("每天60s读懂世界", content)
