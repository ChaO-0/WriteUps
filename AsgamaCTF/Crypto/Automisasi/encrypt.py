flag = "< REDACTED >"

cipher = ""
for x in range(len(flag)):
    for y in range(x):
        for z in range(y):
            cipher += str(ord(flag[z]) + ord(flag[x]) - ord(flag[y]))

with open("encrypted","wb") as f:
    f.write(cipher)
    f.close() 
