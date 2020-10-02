# 複数の例外を受け取る

try :
    print(a)
except ( KeyError, NameError ) as e:
    print("例外発生:" + str(e))
else:
    print("正しい処理です")
