# 例外が発生しない場合、「else」ブロックを実行します

a = 10

try :
    print(a)
except NameError:
    print("例外発生：変数「a」を宣言していません")
else:
    print("変数「a」を宣言しています")
