new = open("output2.txt", "rb").read()

newfile = new.replace(".", "P")
open("output3.txt", "w+").write(newfile)
