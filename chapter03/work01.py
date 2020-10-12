from datetime import datetime, timezone, timedelta

# システムに基づく現在時刻（UTCと同じ意味）
now = datetime.now()
print(now)

# 日本標準時間のタイムゾーンの作成（+9時間）
tz_jst = timezone(timedelta(hours=9))

# 日本標準時間に基づく現在時刻
now_jst = datetime.now(tz=tz_jst)
print(now_jst)
