# 追加書き込み

from datetime import datetime

now = datetime.now()
now_str1 = now.strftime("%Y年%m月%d日%H時%M分%S秒")

f = open("python-level4/chapter05/data/data9.txt", "a")

f.write("[アクセス時刻]  " + now_str1)
f.write("\n")

f.close()
