# 宣言していない変数を利用するので「NameError」例外発生

try :
    print(a)
except NameError:
    print("例外発生：変数「a」を宣言していません")
