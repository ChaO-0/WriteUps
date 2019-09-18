flag = ' 218h, 250h, 190h, 180h, 188h, 1C8h, 3D8h, 188h, 1B8h, 320h, 310h, 1C0h, 180h, 310h, 1B0h, 320h, 328h, 1B8h, 320h, 190h, 1B0h, 1B0h, 330h, 190h, 180h, 330h, 318h, 1C0h, 1A8h, 1A8h, 1C8h, 188h, 1C8h, 310h, 188h, 308h, 310h, 1B0h, 188h, 318h, 190h, 1B8h, 310h, 1B0h, 180h, 308h, 328h, 3E8h'
#2 dup() == 2 times
flag = flag.replace('h','')
flag = flag.replace(' ', '0x')
flag = flag.replace(',', ' ')
flag = flag.split()

newflag = []

for i in flag:
    newflag.append(int(i, 16))

print ''.join([chr(x / 8) for x in newflag])
