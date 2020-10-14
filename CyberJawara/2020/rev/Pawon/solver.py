from z3 import *

vars = [Int(str(i)) for i in range(16, 41)]

s = Solver()

s.add(vars[5] == 45, vars[11] == 45, vars[18] == 45)
s.add(vars[0] == vars[10])
s.add(vars[1] == 101)
s.add(vars[3] == 80)
s.add(vars[2] == 109)
s.add(vars[4] == vars[1])
s.add(vars[6] == 106)
s.add(vars[7] == 111)
s.add(vars[8] == vars[9])
s.add(vars[9] == 83)
s.add(9 + 2 * vars[5] == vars[12])
s.add(vars[23] == vars[17] + 3)
s.add(vars[13] == vars[20])
s.add(vars[14] == 122)
s.add(-134 + 2 * vars[15] == vars[16])
s.add(vars[21] == 84)
s.add(vars[16] == 72)
s.add(vars[20] == 117)
s.add(vars[17] == 53)
s.add(vars[19] == 83)
s.add(vars[22] == 49)
s.add(vars[10] == vars[21])
s.add(-61 + 2 * vars[24] == vars[20])
print s.check()
print s.model()

w = {40 : 89,
 26 : 84,
 38 : 49,
 35 : 83,
 33 : 53,
 36 : 117,
 32 : 72,
 37 : 84,
 31 : 103,
 30 : 122,
 29 : 117,
 39 : 56,
 28 : 99,
 25 : 83,
 24 : 83,
 23 : 111,
 22 : 106,
 20 : 101,
 18 : 109,
 19 : 80,
 17 : 101,
 16 : 84,
 34 : 45,
 27 : 45,
 21 : 45}

test = []

for i in w:
    test.append(i)

serial = ''

for i in range(len(w)):
    serial += chr(w[test[i]])

print serial

# print vars[20]