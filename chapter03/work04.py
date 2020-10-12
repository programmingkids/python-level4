from datetime import datetime, timezone, timedelta

# 年月日時分秒を個別に表示

# 日本標準時間のタイムゾーンの作成（+9時間）
tz_jst = timezone(timedelta(hours=9))

# 日本標準時間に基づく現在時刻
now = datetime.now(tz=tz_jst)

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
