"""
練習問題

例外「ZeroDivisionError」が発生します
try-exceptで例外を補足するようにしてください
例外が発生した場合、以下のように表示します

例外発生：division by zero
"""

try :
    print( 5 / 0 )
except ZeroDivisionError as e:
    print("例外発生：" + str(e))
