from pwn import *

string = 'Hb\xf7}_\x7f4\x7f\x7f_\xffQM\xf0_PP1Ai\x00\x80\x801\x08@\xb4\x00\x00AF\x00E\x00\x02\x00E\x1c\x10\xa8\x01%\x00\x11\x00\xa8\x02\x80\xbaE\x00&\x16\x02\xc1\x00,\x00"\x00'
# p = process("keygen")
p = remote("3.228.124.42", 20007)
p.sendline(string)
p.interactive()