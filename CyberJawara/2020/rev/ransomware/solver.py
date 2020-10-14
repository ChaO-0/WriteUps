table = [x for x in range(256)]
x = 0
y = 0

def init_value():
    global table, x, y
    for i in range(256):
        table[i] = i
    x = 0
    y = 0

def sub_866(a1, a2):
    global table, x, y
    for y in range(256):
        x = (table[y] + x + a1[y % a2]) & 0xff
        table[x], table[y] = table[y], table[x]

    x = 0
    y = 0

def sub_944():
    global x, y, table
    y = (y + 1) & 0xff
    x = (x + table[y]) & 0xff
    table[x], table[y] = table[y], table[x]
    return table[(table[y] + table[x]) & 0xff]

init_value()
anu = [0x72,0x68,0x63,0x6D,0x65,0x6D,0x5F,0x5F,0x63,0xAD,0x65,0x6D,0x5F,0x5F,0xDA,0x43]

sub_866(anu, 16)

nyari_key = open("real_enc_flag/flag.txt.enc", "rb").read()[:32]
key = []

for i in range(32):
    wadoh = sub_944()
    key.append(wadoh ^ ord(nyari_key[i]))

nyari_flag = open("real_enc_flag/flag.txt.enc", "rb").read()[32:]
flag = ''

init_value()
sub_866(key, 32)

for i in range(len(nyari_flag)):
    wadoh = sub_944()
    flag += chr(wadoh ^ ord(nyari_flag[i]))

print flag