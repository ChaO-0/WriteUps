import string

def freefire(apositiveint):
    x = apositiveint // 2
    seen = set([x])
    while x * x != apositiveint:
        x = (x + (apositiveint // x)) // 2
        if x in seen: return False
        seen.add(x)
    return True

enc = open('encrypted.txt', 'rb').read().decode('utf-8').split(", ")
enc = list(map(int, enc))

alphabet = string.ascii_letters + string.digits + "{_}"
#flag: COMPFEST12{ez_pz_lemonade_squeez_a42447}
flag = ""

for i in enc:
    for j in alphabet:
        tmp = i ^ ord(j)
        letter = i ^ tmp
        if(freefire(tmp)):
            flag += chr(letter)
            print(freefire(tmp), chr(letter))
            break

print(flag)