enc = "5b5a4358222121286b587e757f7f756279704f5a7573717f776271707e4e5b446d".decode('hex')
xor = [0x10, 0x11]

flag = ""

for i, j in enumerate(enc):
    flag += chr(ord(j) ^ xor[i % len(xor)])

print flag