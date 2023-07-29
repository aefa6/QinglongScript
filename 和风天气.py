import requests
import json
import notify

#填写下面的信息，loca应填的数字请自行去和风官网查找，使用青龙自带的推送
api = "你的和风天气API key"
loca = "数字，代表你所在位置"

# 和风天气获取
api_url = f"https://devapi.qweather.com/v7/weather/now?location={loca}&key={api}" 
apim_url = f"https://devapi.qweather.com/v7/minutely/5m?location={loca}&key={api}" 
apiw_url = f"https://devapi.qweather.com/v7/warning/now?location={loca}&key={api}" 
apii_url = f"https://devapi.qweather.com/v7/indices/1d?type=3,5,13&location={loca}&key={api}" 
response = requests.get(api_url)
data = json.loads(response.text)
weather = data['now']
responsem = requests.get(apim_url)
datam = json.loads(responsem.text)
weatherm = datam['summary']
responsew = requests.get(apiw_url)
dataw = json.loads(responsew.text)
weatherw = dataw['warning']
responsei = requests.get(apii_url)
datai = json.loads(responsei.text)
weatheri = datai['daily']

if weatherw:
  tip = weatherw[0]['text'] 
else:
  tip = ""

#汇总信息
info = f"""
{weather['text']}，{weather['windDir']}{weather['windScale']}级     
温度:{weather['temp']}°C    体感温度:{weather['feelsLike']}°C    
湿度:{weather['humidity']}%      
能见度:{weather['vis']}KM    
{weatheri[0]['text']}
{weatheri[1]['text']}    
{weatheri[2]['text']}    
预测:{weatherm}    
{tip}
"""
infot = f"""
{weather['obsTime']}
"""
notify.send(infot, info)
