flag = "033_CFLN_PTVX_elmrst"
test = [7,3,14,16,12,3,7,12,6,6,7,11,9,14,28,5,1,21,2,26,]

hai = ""

for i in range(len(flag)):
    hai += chr(ord(flag[test[i] ^ i]))

print hai