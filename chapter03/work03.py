from datetime import datetime

# dateimeオブジェクトの日時情報をもとにして、文字列で表示

now = datetime.now()

# 年月日時分秒
date_str1 = now.strftime("%Y年%m月%d日%H時%M分%S秒")
print(date_str1)

# 年月日
date_str2 = now.strftime("%Y年%m月%d日")
print(date_str2)
