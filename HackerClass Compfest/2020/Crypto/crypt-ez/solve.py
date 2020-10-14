import random
from math import ceil

p = 101
q = 211

enc = open("enc", "rb").read().decode('utf-8')
random.seed(q)

# print(enc)
enc2 = ''
for i in range(10, len(enc) + 10):
    i -= 1
    z = p + q - i
    enc2 += chr(ord(enc[i - 9]) ^ random.randint(i, z))

flag = []
for i in enc2:
    flag.append((ord(i) - random.randint(1,4)) / 5)

print(''.join([chr(round(i)) for i in flag]))

# for i in enc2:
#     print(ord(i), end = ' ')