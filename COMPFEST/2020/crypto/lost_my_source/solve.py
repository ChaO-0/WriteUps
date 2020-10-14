enc = open("encrypted.txt", "rb").read()
known = "COMPFEST{"[::-1]
hai = ''

# print len(enc)
for i in range(31, -1, -1):
    hai += chr(ord(enc[31 - i]) ^ i ^ ord(known[i % len(known)]))

print hai