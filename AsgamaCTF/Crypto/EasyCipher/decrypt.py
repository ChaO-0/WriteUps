from pwn import *

known_flag = "GamaCTF{"
key = "Qk3j4cnmb8"
flag = []
enc = open("encrypted.txt", "rb").read()

log.info("Encrypted flag : {}".format(enc))

for i in range(len(enc) / 2):
    k = enc[i * 2:i * 2 + 2]
    flag.append(k)
newflag = []
for i in range(40):
    newflag.append(flag[i])

newnewflag = []

for i in newflag:
    newnewflag.append(int(i, 16))

log.info("Decrypted hex : {}".format(newnewflag))

realflag = ""

for a in range(len(newnewflag) / len(key)):
    i = a
    for b in range(len(key)):
        realflag += chr(newnewflag[i] ^ ord(key[b]))
        i += len(newnewflag) / len(key)

log.info("Plain text : {}".format(realflag))
