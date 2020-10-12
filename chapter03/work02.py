from datetime import datetime

# 文字列の「日時」に基づいて、dateimeオブジェクト作成

# 年月日時分秒（UTC）
date_str1 = "2018-12-05 9:15:30"

dt_obj1 = datetime.strptime(date_str1,"%Y-%m-%d %H:%M:%S")
print(dt_obj1)


# 年月日時分秒（日本標準時間）
date_str2 = "2018-12-05 9:15:30+0900"

dt_obj2 = datetime.strptime(date_str2,"%Y-%m-%d %H:%M:%S%z")
print(dt_obj2)

# 年月日（日本標準時間）
date_str3 = "2018-5-10+0900"

dt_obj3 = datetime.strptime(date_str3,"%Y-%m-%d%z")
print(dt_obj3)
