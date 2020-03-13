flag = ""
with open("log.txt") as f:
    prev_h = None
    for l in f:
        try:
            arr = eval(l.strip()) # remove whitespace
            if arr[4] == 1:
                if prev_h:
                    for i in range(256):
                        if (prev_h + i) * arr[1] % arr[0] == arr[2]:
                            flag += chr(i)
                            break
                prev_h = arr[2]
        except:
            pass
print(flag)