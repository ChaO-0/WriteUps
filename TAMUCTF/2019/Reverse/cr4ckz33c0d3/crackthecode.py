from pwn import *

alphabet = [48, 49, 50, 51, 52, 53, 54, 55 ,56 ,57]
a1 = [65] * 29
a1[5] = 45
a1[11] = 45
a1[17] = 45
a1[23] = 45
a1[0] = 77
a1[20] = 66
a1[21] = 66
#a1[4] - 48 == 2 * (a1[1] - 48) + 1 && a1[4] - 48 > 7 && a1[9] == a1[4] - (a1[1] - 48) + 2

for i in alphabet:
    for j in alphabet:
        for k in alphabet:
            for l in alphabet:
                if(j - 48 == 2 * (i - 48) + 1 and j - 48 > 7 and k == j - (i - 48) + 2):
                    a1[1] = i
                    a1[4] = j
                    a1[9] = k
                
                if((j + l + i) % 26 == 4 and (i + j) % 11 == 5 and (k + j) % 22 == 18 and (k + l) % 13 == 8):
                    a1[18] = i
                    a1[22] = j
                    a1[27] = k
                    a1[28] = l
                    break
                if(a1[1] + a1[4] * i) % 41 == 5:
                    a1[6] = i
                v1 = ((i + a1[4] + a1[27] - 18) >> 31) >> 28
                if((v1 + i + a1[4] + a1[27] - 18) & 0xF) - v1 == 8:
                    a1[15] = i
code = ""
for i in a1:
    code += chr(i)

print "Passsword: {}".format(code)

r = remote("rev.tamuctf.com", 8189)
r.sendline(code)
r.interactive()
