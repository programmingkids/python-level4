from datetime import datetime, timedelta

format_str = "%Y年%m月%d日"

# 今日
now = datetime.now()
print(now.strftime(format_str))

# 明日
tomorrow = now + timedelta(days=1)
print(tomorrow.strftime(format_str))

# 昨日
yesterday = now + timedelta(days=-1)
print(yesterday.strftime(format_str))

# 1年後の今日
next_year = now + timedelta(days=365)
print(next_year.strftime(format_str))
