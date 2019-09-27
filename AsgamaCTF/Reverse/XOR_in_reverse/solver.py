enc = "a)))KkFmQ*wFz)TixK*||"
flag = []

for i in enc:
	flag.append(chr(ord(i) ^ 25))

print ''.join(flag)
