def clear():
    var = '''
        CE
        D2
        83
        76
        96
        F6
        F0
        BE
        F3
        33
        8F
        6A
        3A
        F5
        2F
        BF
        7E
        EE
        06
        FC
        DA
        2D
        5B
        3F
        F5
        BE
        D0
        A7
        7E
        73
        95
        3F
        A0
        4A
        72
        65
        F5
        B3
        AF
        BF
        4B
        3C
        A0
        6C
        CA
        15
        E4
        BF
        6E
        A7
        AD
        11
        C1
        38
        F0
        3F
        F6
        EB
        4E
        77
        9E
        38
        1F
        40
        03
        78
        0B
        24
        28
        1E
        1B
        C0
        DE
        54
        A4
        C2
        D8
        3A
        42
        C0
        BB
        7E
        C1
        6E
        D8
        A6
        26
        40
        53
        96
        21
        8E
        75
        61
        43
        40
        00
        00
        00
        00
        00
        C0
        58
        40
        '''
    var = var.replace("\n", "")
    var = var.replace("        ", " ")
    var = var.replace(" ", " 0x")
    var = var.split(" ")
    var = var[1:-1]
    start = 0
    newvar = []
    #print "Var : ", var
    while start < len(var):
        newvar.append(var[start])
        start += 8
    #print "Newvar : ", newvar
    return newvar

var = []

for i in clear():
    var.append(int(i, 16)) 
print var
flag = "@"
local_84 = 0
local_88 = 0
i = 0
#while local_84 < 13:
#    local_70 = 0.0
#    local_7c = 0
#    while local_7c < 13:
#        local_70 = (local_84 - 6) * local_70 + var[local_7c]
#        local_7c += 1
#        
#    if local_70 <= 0.0:
#        local_70 -= 0.5
#    else:
#        local_70 += 0.5
#
#    local_88 =  local_88 + ord(flag[i]) - local_70
#    local_84 += 1
#    i += 1
local_7c = 0
local_70 = 0.0
while local_7c < 13:
    local_70 = (local_84 - 6) * local_70 + var[local_7c]
    print var[local_7c], local_70
    local_7c += 1
if local_70 <= 0.0:
    local_70 -= 0.5
else:
    local_70 += 0.5

print local_70