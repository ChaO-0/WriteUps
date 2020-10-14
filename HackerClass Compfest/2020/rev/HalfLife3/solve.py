#101 atau 211 seednya di soal crypto random
import string

def anu1(a):
    return ''.join([chr((ord(i)-97-1-(1^2))%26+97) for i in a])

def int2base(x, base):
    digs = string.digits + string.ascii_letters
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

print anu1(int2base(16166842727364078278681384436557013, 36))