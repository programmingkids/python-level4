# 例外の情報を一時変数で受けとる

person = {
    "name" : "Bob",
    "age" : 15,
}

try :
    print(person["hobby"])
except KeyError as e:
    print("存在しないキーを指定しました:" + str(e))
else:
    print("キーが存在します")
finally:
    print("必ず実行します")
