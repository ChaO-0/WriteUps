from pwn import *
import struct

def float_to_int(float_num):
	#payload = struct.unpack("I", struct.pack("<f",float_num))[0]
	#return str(payload)
	payload = u32(struct.pack('<f', float_num))
        return str(payload)

if __name__ == "__main__":
	r = remote("152.118.201.254", 18015)
	r.recvuntil("Clue: ")
	num = r.recvline()
	payload = float_to_int(float(num))
	log.info("Predicted number: {}". format(payload))

	r.sendline(payload)
	r.interactive()
