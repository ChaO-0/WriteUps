flag = "0Eh, 17h, 1Dh, 14h, 42h, 0Fh, 3Ch, 0FCh, 17h, 40h, 39h, 28h, 1Eh, 0FDh, 3Eh, 31h, 26h, 1Eh, 0FDh, 1Fh, 2Ch, 3Eh, 3Dh, 2Eh, 2Ch, 31h, 29h, 0FAh, 1Ah, 2Bh, 11h, 38h, 36h, 0FCh, 0Eh, 46h, 0"

flag = flag.replace('h','')
flag = flag.replace(' ', '0x')
flag = flag.replace(',', ' ')
flag = flag.split()
newflag = []
for i in flag:
    newflag.append(int(i, 16))

print newflag

known_pattern = "GKSK{"
known_flag = [0xe, 0x17, 0x1d, 0x14, 0x42]
repeat = []

for i in range(len(known_pattern)):
    repeat.append(chr(ord(known_pattern[i]) - known_flag[i]))
    
print repeat

pattern = ["9", "4", "6", "7"]
realflag = []


for i in range(len(flag)):
    kunci = ord(pattern[i % len(pattern)])
    realflag.append(chr((newflag[i] + kunci) % 256))
    
print ''.join(realflag)
