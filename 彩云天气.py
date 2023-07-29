# @author Sten
# 作者仓库:https://github.com/aefa6/QinglongScript.git
# 觉得不错麻烦点个star谢谢

import requests
import json
import notify 
#填写下面的信息，经纬度请自行百度，使用青龙自带的推送
key = "你的彩云天气API key"
lon = "你所在位置的经度"
lat = "你所在位置的纬度"

#下面的不用管了
api_url = f"https://api.caiyunapp.com/v2.6/{key}/{lon},{lat}/weather?alert=true&realtime&minutely" 
response = requests.get(api_url)
data = json.loads(response.text)
weather = data['result']

if weather['alert']['content']:
  tip = weather['alert']['content'][0]['description'] 
else:
  tip = ""

info = f"""
实时天气:  
天气现象:{weather['realtime']['skycon']}    
温度:{weather['realtime']['temperature']}°C     
体感温度:{weather['realtime']['apparent_temperature']}°C    
湿度:{weather['realtime']['humidity']}      
能见度:{weather['realtime']['visibility']}KM    
紫外线强度:{weather['realtime']['life_index']['ultraviolet']['desc']}   
空气质量:{weather['realtime']['air_quality']['description']['chn']}     
总体感觉:{weather['realtime']['life_index']['comfort']['desc']}     
    
全天:
温度:{weather['daily']['temperature'][0]['min']} - {weather['daily']['temperature'][0]['max']}°C, 白天温度:{weather['daily']['temperature_08h_20h'][0]['min']} - {weather['daily']['temperature_08h_20h'][0]['max']}°C, 夜间温度:{weather['daily']['temperature_20h_32h'][0]['min']} - {weather['daily']['temperature_20h_32h'][0]['max']}°C    
紫外线强度{weather['daily']['life_index']['ultraviolet'][0]['desc']},总体感觉{weather['daily']['life_index']['comfort'][0]['desc']}      
    
预测:{weather['minutely']['description']},{weather['hourly']['description']}    
{tip}
"""

print(info)
notify.send("彩云天气", info)
