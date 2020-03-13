def solve():
    flag = "2Y6^3RJ^/v6mV^346DT^^q062l"
    flag = list(flag)
    for i in range(len(flag)):
        flag[i] = chr(ord(flag[i]) + 1)

    condition = [0,0,1,1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1]

    for i in range(0, 25, 2):
        if condition[i] == 1:
            flag[i], flag[i + 1] = flag[i + 1], flag[i]

    return ''.join(flag)

if __name__ == "__main__":
    print "Flag : GKSK{%s}" % solve()