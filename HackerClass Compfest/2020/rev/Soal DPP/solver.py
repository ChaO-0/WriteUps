enc = 120290679218832191630163797978118096998325980286646140214484761791004452553
shift = 240

flag = []

def master(f, xx, yy=0):
    if yy == len(xx):
        return xx
    f(xx, yy)
    return master(f, xx, yy + 1)

def jj(xx):
    def ff(aa, bb):
        aa[bb] = ((0xF & aa[bb]) << 4) + ((aa[bb] >> 4))

    return master(ff, xx)

for i in range(240, 0, -8):
    letter = enc >> i
    _next = letter << i
    enc -= _next
    flag.append(letter)

flag.append(enc)
flag = jj(flag)
dec = []

for i, j in enumerate(flag):
    dec.append(j - (i + 1))

print "Flag: %s" % ''.join(chr(x) for x in dec)