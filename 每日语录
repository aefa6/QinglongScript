# @author Sten
# 作者仓库:https://github.com/aefa6/QinglongScript.git
# 觉得不错麻烦点个star谢谢
# 用的故梦api，https://api.gumengya.com/
# 要自定义请自行修改15、16行，默认是2条随机一言和2条随机笑话
import requests
import json
import notify
Yiurl = 'https://api.gumengya.com/Api/YiYan?format=json' #随机一言
Xiurl = 'https://api.gumengya.com/Api/Xiaohua?format=json' #随机笑话
Dourl = 'https://api.gumengya.com/Api/Dog?format=json' #随机舔狗日记
Waurl = 'https://api.gumengya.com/Api/WaSentence?format=json' #随机文案
Lourl = 'https://api.gumengya.com/Api/LoveSentence?format=json' #随机土味情话

urls = [Yiurl, Xiurl] # 按照格式填写你要推送的内容对应的url
count = 2 # 相同类型推文的数量

contents = ""
for url in urls:
	for i in range(count):
  		response = requests.get(url)
  		data = json.loads(response.text)
  		contents += data['data']['text'] + "\n" + "\n"
notify.send("每日语录", contents)
