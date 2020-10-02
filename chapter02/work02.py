# lower

names = ["John", "anna", "nancy","bOB", "ELsa"]

for name in names :
    # 小文字に変換
    print(name.lower())


"""
# リストコンプリヘンション
names = [name.lower() for name in names]
print(names)
"""

"""
# マップ関数とラムダ式
names = list(map(lambda name : name.lower(), names))
print(names)
"""
