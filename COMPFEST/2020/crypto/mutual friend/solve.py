from pwn import *

p = remote("128.199.157.172", 27268)
#print p.recv()

p.sendline('')
print p.recv()
