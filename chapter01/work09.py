"""
練習問題

例外「KeyError」が発生します
try-exceptで例外を補足するようにしてください
例外が発生した場合、以下のように表示します

例外発生:'理科'
"""

scores = {
    "国語" : 90,
    "数学" : 82,
    "英語" : 95,
}

try :
    print(scores["理科"])
except KeyError as e:
    print("例外発生:" + str(e))
