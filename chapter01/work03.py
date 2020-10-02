# 例外が発生すると「except」ブロックを実行
# 最後に「finally」ブロックを必ず実行

person = {
    "name" : "Bob",
    "age" : 15,
}

try :
    print(person["hobby"])
except KeyError:
    print("存在しないキーを指定しました")
else:
    print("キーが存在します")
finally:
    print("必ず実行します")
