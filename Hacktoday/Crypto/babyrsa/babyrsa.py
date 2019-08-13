#flag = open("flag").read()
#m = int(flag.encode("hex"), 0x16)
from Crypto.Util.number import *
c = 34800025394951925292080924856671179486606568805409940926874542700517211148095
e = 0x10001
n = 0x54012066b18843995165c3c0d783aa9e31e796f6928ea4bfe0728b1d1bad6271
p = 11630107594679429833
q = 16760491439280901423

phi = (p - 1) * (q - 1)
d = inverse(e, phi)
m = pow(c, d, n)
m =int(str(m), 16)
print str(m).decode('hex')
