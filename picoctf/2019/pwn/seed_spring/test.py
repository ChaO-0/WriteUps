from pwn import *
import ctypes

LIBC = ctypes.cdll.LoadLibrary('/lib/x86_64-linux-gnu/libc.so.6')

BINARY = './seed_spring'

context.binary = BINARY
context.terminal = ['tmux', 'splitw', '-v']

for i in range(100):

	sh = remote('2019shell1.picoctf.com', 21871)
	try:
		LIBC.srand(LIBC.time(0)-i)

	for i in range(30):
		payload = LIBC.rand() & 0xF
		print str(i) + str(payload)
		sh.sendlineafter(': ', str(payload))
      

	sh.interactive()
	except:
		print 'Wrong'