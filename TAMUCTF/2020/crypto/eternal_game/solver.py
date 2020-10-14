from pwn import *
from hashpumpy import hashpump

def solve():
    p = remote("challenges.tamuctf.com", 8812)
    # p = process(["python", "chall.py"])

    p.sendline("1")
    p.sendline("3")
    p.recvuntil("quit\n")
    
    known_hash = p.recvline()[:-1]
    log.info("Known Hash: {}".format(known_hash))

    for key_length in range(1, 0xb):
        p.sendline("2")
        new_hash, msg = hashpump(known_hash, '1', '1306172139783549808932216282612057073445238267608', key_length)
        p.sendline(msg)
        p.sendline(new_hash)
        print key_length

    p.interactive()

if __name__ == "__main__":
    solve()