from datetime import datetime, timezone, timedelta

# 日本標準時間のタイムゾーンの作成（+9時間）
tz_jst = timezone(timedelta(hours=9))

format_str = "%Y年%m月%d日"

# 今日
now = datetime.now(tz=tz_jst)
print("今日:" + now.strftime(format_str))

# 明日
tomorrow = now + timedelta(days=1)
print("明日:" + tomorrow.strftime(format_str))

# 昨日
yesterday = now + timedelta(days=-1)
print("昨日:" + yesterday.strftime(format_str))

# 1年後の今日
next_year = now + timedelta(days=365)
print("1年後:" + next_year.strftime(format_str))
