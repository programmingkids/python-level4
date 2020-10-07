"""
練習問題

リスト「members」があります。

リストの要素を改行を行ったうえで、以下のファイルに書き込んでください。ファイル内には以下のように書き込みます

■ファイル名
python-level4/chapter07/data/data10.txt

Micky
Donald
Elsa
Anna
Ariel

"""

members = ["Micky","Donald","Elsa","Anna","Ariel"]

f = open("python-level4/chapter07/data/data10.txt", "w")

for m in members :
    f.write(m + "\n")
f.close()
