"""
練習問題

変数「date_str」には「2005-04-15 10:30」の文字列が代入されています。

この文字列に基づいて、datetimeオブジェクトを作成してください。
そのうえで、以下のように表示する処理を作成してください

メソッド「strptime」では「"%Y-%m-%d %H:%M"」で解析します
メソッド「strftime」では「"%Y年%m月%d日%H時%M分"」で表示します

2005年04月15日10時30分
"""

from datetime import datetime

date_str = "2005-04-15 10:30"

