from pwn import *
v5 = ""
v2 = ord('H')
flag = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
key = "[OIonU2_<__nK<KsK"
iterator = 0
while True:
	for i in flag:
		if(((ord(i) + 12) * v2 + 17) % 70 + 48) == ord(key[iterator]):
			v5 += i
			v2 = ord(key[iterator])
			iterator += 1
			break
	if(len(v5) == len(key)):
		break
v5 = v5[:-1]
print "Key: {}".format(v5)
r = remote("rev.tamuctf.com", 7223)
r.sendline(v5)
r.interactive()
