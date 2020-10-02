# 複数の例外を受け取る

try :
    print(a)
except KeyError as e:
    print("存在しないキーを指定しました:" + str(e))
except NameError as e:
    print("変数が存在しません:" + str(e))
else:
    print("正しい処理です")
