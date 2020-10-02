# 例外を発生

age = 15

try :
    if age < 18 :
        raise Exception("18歳未満は選挙権がありません")
except Exception as e :
    print("例外発生:" + str(e))
else :
    print("選挙権があります")
