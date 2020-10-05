# メソッド「readlines」

f = open("python-level4/chapter05/data/data3.txt", "r")

lines = f.readlines()

for line in lines :
    print(line, end="")

f.close()
