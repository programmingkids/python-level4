# メソッド「readline」

f = open("python-level4/chapter05/data/data4.txt", "r")

line = f.readline()

while line :
    print(line, end="")
    line = f.readline()
    
f.close()
