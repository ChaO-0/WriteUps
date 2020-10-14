from Crypto.Util.number import inverse
from fractions import *

e = 43
n = 2531257
c = "906851 991083 1780304 2380434 438490 356019 921472 822283 817856 556932 2102538 2501908 2211404 991083 1562919 38268"
c = c.split(" ")
c = map(int, c)
p = 509
q = 4973
phi = (p - 1) * (q - 1)
d = inverse(e, phi)
m = []
for i in c:
	m.append(pow(i, d, n))
print  m

plain = [103, 105, 103, 101, 109, 123, 83, 97, 118, 97, 103, 101, 95, 83, 105, 120, 95, 70, 108, 121, 105, 110, 103, 95, 84, 105, 103, 101, 114, 115, 125]
flag = ""
for i in plain:
	flag += chr(i)
print "Decoded flag : ", flag
