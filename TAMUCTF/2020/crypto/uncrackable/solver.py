cipher = [0xe3, 0xf8, 0xe5, 0x11, 0x0e, 0x29, 0xe6, 0xfd, 0xe3, 0x1a, 0x08, 0x61, 0xf0, 0xa4, 0xdd, 0x13, 0x53, 0x0d, 
0xb5, 0xff, 0xdd, 0x17, 0x11, 0x3b, 0xe6, 0xc2, 0xdd, 0x1c, 0x02, 0x2f]

xor = [132, 145, 130, 116, 99, 82]

flag = []
for _ in range(len(cipher)):
    flag.append(chr(cipher[_] ^ xor[_ % len(xor)]))

print ''.join(flag)