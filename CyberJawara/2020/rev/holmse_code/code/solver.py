import re
from pwn import disasm

flag = ''

for i in range(0, 288):
    bjyr = open("code" + str(i), "rb").read().encode('hex')

    shellcode = re.findall(r"5858488b4424108a10(.*?)751048c7c7", bjyr)[0]
    cmp = disasm(bytearray.fromhex(shellcode))
    op = re.findall(r"                (.*)    ", cmp)[0]
    # print op
    duar = re.findall(r"    dl, (.*)", cmp)
    # print duar
    if op == 'sub':
        flag += chr((int(duar[0], 16) + int(duar[1], 16)) % 256)
    elif op == 'add':
        flag += chr((int(duar[1], 16) - int(duar[0], 16)) % 256)
    elif op == 'xor':
        flag += chr((int(duar[0], 16) ^ int(duar[1], 16)) % 256)

print flag