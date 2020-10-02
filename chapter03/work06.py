"""
練習問題

変数「date_str」には「2005-10-29」の文字列が代入されています。

この文字列に基づいて、datetimeオブジェクトを作成してください。
そのうえで、以下のように表示する処理を作成してください

2005年10月29日
"""

from datetime import datetime

date_str = "2005-10-29"

dt_obj = datetime.strptime(date_str,"%Y-%m-%d")
print(dt_obj.strftime("%Y年%m月%d日"))
