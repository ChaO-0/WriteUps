from Crypto.Util.number import *
import string

digs = string.digits + string.ascii_letters

def int2base(x, base):
    if x < 0:
        sign = -1
    elif x == 0:
        return digs[0]
    else:
        sign = 1

    x *= sign
    digits = []

    while x:
        digits.append(digs[int(x % base)])
        x = int(x / base)

    if sign < 0:
        digits.append('-')

    digits.reverse()

    return ''.join(digits)

e = 0x10001
n = 0x54012066b18843995165c3c0d783aa9e31e796f6928ea4bfe0728b1d1bad6271
c = 35656204442282500905978583616900374314676740601677077259046538294788646924415

p = 16760491439280901423
q = 11630107594679429833

assert pow(p,2)*pow(q,2) == n
assert isPrime(p) == True
assert isPrime(q) == True

phi = p*q*(p-1)*(q-1)
d = inverse(e,phi)

flag = int2base(pow(c,d,n),0x16)
print flag.decode("hex")

