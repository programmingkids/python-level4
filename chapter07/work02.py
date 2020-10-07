"""
練習問題

例外「IndexError」が発生します
try-exceptで例外を補足するようにしてください
例外が発生した場合、以下のように表示します

例外発生：list index out of range
"""

colors = ["red","blue","yellow","pink"]

try :
    print(colors[10])
except IndexError as e:
    print("例外発生：" + str(e))
