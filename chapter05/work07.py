# write

teams = ["Giansts","Tigers","Baystars","Swallows","Dragons","Carp"]

f = open("python-level4/chapter05/data/data7.txt", "w")

for team in teams:
    f.write(team)
    f.write("\n")

f.close()
