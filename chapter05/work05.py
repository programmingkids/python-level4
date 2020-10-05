# try-except

try:
    f = open("python-level4/chapter05/data/data5.txt", "r")
except FileNotFoundError as e:
    print("例外発生：ファイルが存在しません")
else:
    lines = f.readlines()
    for line in lines:
        print(line, end="")
    f.close();
