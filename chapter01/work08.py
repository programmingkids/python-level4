# オリジナル例外クラスの作成

class MyError(Exception):
    pass


name ="John"

try :
    if name != "Bob" :
        raise MyError("MyErrorが発生しました")
except MyError as e :
    print("例外発生：" + str(e))
