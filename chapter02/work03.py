# strip

names = ["    John  ", "  Anna    ", "   Bob "]

for name in names :
    # 前後の空白を取り除く
    print(name.strip())

"""
# リストコンプリヘンション
names = [name.strip() for name in names]
print(names)
"""

"""
# マップ関数とラムダ式
names = list(map(lambda name : name.strip(), names))
print(names)
"""
