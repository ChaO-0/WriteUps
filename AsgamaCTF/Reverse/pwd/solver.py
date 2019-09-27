flag = [170, 229, 141, 177, 191, 234, 222, 205, 185, 223, 
  172, 201, 225, 223, 156, 129, 249, 142, 129, 160, 
  177, 157, 209, 161, 176, 173, 229, 142, 156, 187]

key = [0xDE, 0xAD, 0xBE, 0xEE, 0xEF]

new = []
for i in range(30):
    new.append(chr(flag[i] ^ key[i % 5]))

print ''.join(new)