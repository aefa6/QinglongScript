# @author Sten
# 作者仓库:https://github.com/aefa6/QinglongScript.git
# 觉得不错麻烦点个star谢谢
# 使用方法：第10行填入阳历(公历)生日，30行可以自定义需要的重要日名称和日期（请按照模板中现有的格式填写,多个请用@分隔）。需要阴历(农历)倒计时请看另一个版本。

import notify
from datetime import datetime

# 在这里填入你的阳历生日，格式为 "月-日"
solar_birthday_str = "01-01"

# 获取当前日期（并转换为仅日期格式）
now = datetime.now().date()

# 获取今年的阳历生日
solar_birthday_this_year = datetime.strptime(f"{now.year}-{solar_birthday_str}", "%Y-%m-%d").date()

# 如果今年的阳历生日已经过去，那么下一次阳历生日就是明年的生日
if now > solar_birthday_this_year:
    next_solar_birthday = datetime.strptime(f"{now.year + 1}-{solar_birthday_str}", "%Y-%m-%d").date()
else:
    next_solar_birthday = solar_birthday_this_year

# 计算距离下一次阳历生日还有多少天
solar_days_left = (next_solar_birthday - now).days

info = f"距离你下一次的阳历生日还有 {solar_days_left} 天。"

# 在这里填入你的自定义事件的名称和日期，格式为 "事件名:月-日@事件名:月-日@..."
custom_event_str = "纪念日:01-01@毕业日:01-01"

# 分割多个自定义事件
custom_events = custom_event_str.split("@")

for custom_event in custom_events:
    # 获取自定义事件的名称和日期
    custom_event_name, custom_event_date_str = custom_event.split(":")

    # 获取今年的自定义事件日期
    custom_event_date_this_year = datetime.strptime(f"{now.year}-{custom_event_date_str}", "%Y-%m-%d").date()

    # 如果今年的自定义事件日期已经过去，那么下一次自定义事件日期就是明年
    if now > custom_event_date_this_year:
        next_custom_event_date = datetime.strptime(f"{now.year + 1}-{custom_event_date_str}", "%Y-%m-%d").date()
    else:
        next_custom_event_date = custom_event_date_this_year

    # 计算距离下一次自定义事件还有多少天
    custom_event_days_left = (next_custom_event_date - now).days

    info += f" 距离 {custom_event_name} 还有 {custom_event_days_left} 天。"

# 发送通知
notify.send("重要日倒计时", info)
