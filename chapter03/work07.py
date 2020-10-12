"""
練習問題

今日から、15日後の日時を表示する処理を作成してください

日本標準時間の現在時刻に基づいて、「datetime」オブジェクトを作成します
その上で、「timedelta」を利用して、15日後の日付を作成します

そのうえで、以下のように表示する処理を作成してください

2018年12月15日10時11分07秒

※実行結果は、今日から15日後の日時です。年月日時分秒を含めて表示してください
"""

from datetime import datetime, timezone, timedelta

# 日本標準時間のタイムゾーンの作成（+9時間）
tz_jst = timezone(timedelta(hours=9))

now = datetime.now(tz=tz_jst)
next_15_day = now + timedelta(days=15)

print(next_15_day.strftime("%Y年%m月%d日%H時%M分%S秒"))
