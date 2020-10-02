"""
練習問題

今日から、15日後の日付を表示する処理を作成してください

現在日に基づいて、「datetime」オブジェクトを作成します
その上で、「timedelta」を利用して、15日後の日付を作成します

そのうえで、以下のように表示する処理を作成してください

※実行結果は、今日から15日後の日付です。以下のように年月日を含めて表示してください

2018年12月15日
"""

from datetime import datetime, timedelta

now = datetime.now()
next_15_day = now + timedelta(days=15)

print(next_15_day.strftime("%Y年%m月%d日"))
