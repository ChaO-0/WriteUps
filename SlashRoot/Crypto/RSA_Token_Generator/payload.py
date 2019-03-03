from pwn import *

r = remote("103.200.7.156", 1003)

r.recvuntil(">>> ")
r.sendline("2")

for i in range(5):
	r.recvuntil("e = ")
	e = r.recvline()
	e = int(e[:-1])

	r.recvuntil("n = ")
	n = r.recvline()
	n = int(n[:-1])

	r.recvuntil("c = ")
	c = r.recvline()
	c = int(c[:-1])

	p = 1000
	while True:
		if(pow(p, e, n) == c):
			break
		p +=1
	r.sendline(str(p))
	print "p = ", p

r.interactive()
