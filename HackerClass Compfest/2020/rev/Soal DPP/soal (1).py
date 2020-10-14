def pw(xx, yx=0, xy=0, xjl=None, llx=None):
    if xjl is None:
        llx=xx.pop
        xjl=jlx(xx)
    if yx < xjl:
        print("xy: ", xy)
        print("yx: ", yx)
        return pw(xx, yx+1, xy + (llx() << (yx << 3)), xjl, llx)
    return xy

jlx = len


def master(f, xx, yy=0):
    if yy == len(xx):
        return xx
    f(xx, yy)
    return master(f, xx, yy + 1)

jxl = ord

def wg(xy):
    fgx = []
    i = 3
    fxg = getattr(fgx, "append")
    for _ in map(fxg, map(jxl, xy)):
        i <<= i ^ i
    return fgx

sw = "{}(gw)".format

def mm():
    pass

x = input("Enter an input:")

def hh(xx):
    def ff(aa, bb):
        aa[bb] += (bb + 0b1) if (bb & 0o1) else (bb | 0x1)

    return master(ff, xx)

ww = exec

def jj(xx):
    def ff(aa, bb):
        aa[bb] = ((0xF & aa[bb]) << 4) + ((aa[bb] >> 4))

    return master(ff, xx)

gw = wg(x)


def kl(xx):
    ww(sw(xx))

def eh(xx):
    def ff(aa, bb):
        aa[bb] -= (bb + 0b1) if (bb & 0o1) else (bb | 0x1)

    return master(ff, xx)

kl("h"*2)

def wiwi(x):
    if x == 0:
        return 1
    else:
        return x * wiwi(x-1)

kl("jj")
print(gw)
print(pw(gw))

if pw(gw) == 120290679218832191630163797978118096998325980286646140214484761791004452553:
    print("The flag is", x)
else:
    print("That doesn't look right")
