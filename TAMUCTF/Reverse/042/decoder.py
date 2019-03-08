asm = '''movb    $65, -16(%rbp)
        movb    $53, -15(%rbp)
        movb    $53, -14(%rbp)
        movb    $51, -13(%rbp)
        movb    $77, -12(%rbp)
        movb    $98, -11(%rbp)
        movb    $49, -10(%rbp)
        movb    $89, -9(%rbp)'''
asm = asm.replace("movb", "")
asm = asm.replace("$", "")
asm = asm.replace("(%rbp", "")
asm = '65 53 53 51 77 98 49 89'
asm = asm.split(" ")
asm = map(int, asm)
flag = []
for i in asm:
	flag.append(chr(i))
print ''.join(flag)
