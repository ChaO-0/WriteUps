import random

def solve():
    file = open('flag.pdf.enc', 'rb').read()
    dec = open('flag.pdf', 'wb')
    seed = 1588453271
    random.seed(seed)
    file = file.replace(b'ransom', b'')
    unfuck = ''

    for char in file:
        unfuck += chr(char ^ random.randint(0, 255))

    dec.write(unfuck.encode('charmap'))
    dec.close()
    # print(file)

if __name__ == "__main__":
    solve()