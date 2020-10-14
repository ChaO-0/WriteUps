#fungsi terus jalan sampe input abis
def pw(xx, yx=0, xy=0, xjl=None, llx=None):
    if xjl is None:
        llx=xx.pop
        xjl=jlx(xx)
    if yx < xjl:
        print("yx: ", yx)
        print("xy: ", xy)
        return pw(xx, yx+1, xy + (llx() << (yx << 3)), xjl, llx)
    return xy

jlx = len
jxl = ord

# Fungsi untuk ngubah karakter ke dalam bentuk ascii code
def wg(xy):
    fgx = []
    i = 3
    fxg = getattr(fgx, "append")
    for _ in map(fxg, map(jxl, xy)):
        i <<= i ^ i
    return fgx


x = input("Enter an input:")

# input di ubah ke ascii
gw = wg(x)
print(pw(gw))

# ? len flag kira kira 30 atau 31
# [68, 21, 5, 69, 180, 180, 165, 197, 163, 195, 104, 56, 211, 86, 230, 88, 7, 87, 116, 40, 71, 136, 164, 149, 215, 151, 41, 244, 152, 166, 201]
# C
if pw(gw) == 120290679218832191630163797978118096998325980286646140214484761791004452553:
    print("The flag is", x)
else:
    print("That doesn't look right")
