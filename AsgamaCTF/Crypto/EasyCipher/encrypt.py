#!/usr/bin/env python2

key = "Qk3j4cnmb8"
flag = "***REDACTED***"


if (len(flag) % len(key) != 0):
	n = len(key) - len(flag) % len(key)
	for i in range(n):
		flag += " "
h = []
for a in range(len(key)):
	i = a
	for b in range(len(flag)/len(key)):
		h.append(ord(flag[i])^ ord(key[a]))
		i += len(key)

encrypted = ""
for j in range(len(h)):
	encrypted +="%02x" % h[j]

f = open('encrypted.txt','w+')print enc
f.write(encrypted)
f.close() 
