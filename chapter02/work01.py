# upper

names = ["John", "anna", "nancy","bOB", "ELsa"]

for name in names :
    # 大文字に変換
    print(name.upper())


"""
# リストコンプリヘンション
names = [name.upper() for name in names]
print(names)
"""

"""
# マップ関数とラムダ式
names = list(map(lambda name : name.upper(), names))
print(names)
"""
