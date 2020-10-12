from datetime import datetime, timezone, timedelta

# dateimeオブジェクトの日時情報をもとにして、文字列で表示

# 日本標準時間のタイムゾーンの作成（+9時間）
tz_jst = timezone(timedelta(hours=9))

# 日本標準時間に基づく現在時刻
now = datetime.now(tz=tz_jst)

# 年月日時分秒
date_str1 = now.strftime("%Y年%m月%d日%H時%M分%S秒")
print(date_str1)

# 年月日
date_str2 = now.strftime("%Y年%m月%d日")
print(date_str2)
