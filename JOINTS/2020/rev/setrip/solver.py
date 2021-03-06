import string

def solve():
    v10 = [0x2F, 0x7B, 0x7D, 0x2D, 0x3A, 0x27, 0x0F, 0x0D, 0x7D, 0x2D, 0x3A, 0x27, 0x33, 0x7B, 0x41, 0x27, \
            0x2B, 0x10, 0x2D, 0x2B, 0x33, 0x2D, 0x3A]
    v9 = [0x2F, 0x7B, 0x7D, 0x2D, 0x3A, 0x27, 0x0F, 0x0D, 0x7D, 0x2D, 0x3A, 0x27, 0x33, 0x7B, 0x41, 0x27, \
            0x2B, 0x10, 0x2D, 0x2B, 0x33, 0x2D, 0x3A]

    i = 0
    while True:
        v2 = i
        if v2 >= len(v10): break
        v3 = v10[i]
        v4 = v3 + 56
        v3 = (((v3 - 200) >> 31) >> 25)
        v10[i] = (v3 - v3 + v4) & 0x7f
        i += 1
    print v10
    print ''.join(chr(x) for x in v10)

def brute(var, idx):
    v10 = [0x2F, 0x7B, 0x7D, 0x2D, 0x3A, 0x27, 0x0F, 0x0D, 0x7D, 0x2D, 0x3A, 0x27, 0x33, 0x7B, 0x41, 0x27, \
            0x2B, 0x10, 0x2D, 0x2B, 0x33, 0x2D, 0x3A]
    v9 = [0x2F, 0x7B, 0x7D, 0x2D, 0x3A, 0x27, 0x0F, 0x0D, 0x7D, 0x2D, 0x3A, 0x27, 0x33, 0x7B, 0x41, 0x27, \
            0x2B, 0x10, 0x2D, 0x2B, 0x33, 0x2D, 0x3A]

    i = 0
    while True:
        v2 = i
        if v2 >= len(var):
            break

        v3 = ord(var[i])
        v4 = v3 - 56
        v3 = (((v3 + 200) >> 31) >> 25)
        v10[idx] = (((v3 + v4) & 0x7f) - v3)
        i += 1
    return v10[idx] == v9[idx]

if __name__ == "__main__":
    shit = string.ascii_letters + string.digits + "_"
    flag = ''

    for i in range(23):
        for j in shit:
            if brute(j, i) is True:
                flag += j
                break

    print flag