from pwn import *

p = process("./world_war")
print p.recvuntil("==")
