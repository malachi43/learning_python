import os
import dbm
import wc

fout = open("output.txt", "w")
fout.write("I'm currently learning python\n")
fout.write("I want to go into Machine Learning\n")
fout.close()


fin = open("output.txt")

for line in fin:
    print(line)


def walk(dirname):
    if os.path.isdir(dirname) == False:
        return
    else:
        print("traversing " + "'" + dirname + "'" + " directory...")
        for file in os.listdir(dirname):
            path = os.path.join(dirname,file)
            if os.path.isfile(path):
                print("file:", file)
            else:
                walk(path)




db = dbm.open("countries_capital", "c")
db["Nigeria"] = "Abuja"
db["Seychelles"] = "Victoria"
db["Ghana"] = "Accra"
db["Zambia"] = "Lusaka"
db["Zimbabwe"] = "Harare"

print("COUNTRIES","CAPITAL",sep = "\t")
print("--------------------------")
for key in db.keys():
    print(key, db[key],sep = "\t")

db.close()

filename = "."
cmd = "ls -l " + filename
fp = os.popen(cmd)
res = fp.read()
print(res)
stat = fp.close()
print(stat)
