# writelines

rivers = ["ナイル川","アマゾン川","長江","ミシシッピ川","信濃川"]

f = open("python-level4/chapter05/data/data8.txt", "w")

f.writelines("\n".join(rivers))

f.close()
