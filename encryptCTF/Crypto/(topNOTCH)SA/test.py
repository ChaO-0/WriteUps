from Crypto.Util.number import *

n = """7f:fd:2b:1a:a7:27:47:f6:a0:1b:9f:96:77:78:7b:
    a1:72:90:93:3e:3a:46:64:0c:ee:55:38:34:32:09:
    ab:d1"""
n = n.replace("\n","")
n = n.replace(":", "")
n = n.replace(" ", "")
n = int(n, 16)
e = 65537
c = "369ad6199548d8181c26d112d1061008c056f08c75339366435046a9a8fbf295"
c = int(c, 16)
p = 194038568404418855662295887732506969011
q = 298348117320990514224871985940356407403
phi = (p - 1) * (q - 1)
d = inverse(e, phi)
m = pow(c, d, n)

print long_to_bytes(m)
