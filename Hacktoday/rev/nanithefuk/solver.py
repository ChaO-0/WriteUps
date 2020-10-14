from subprocess import Popen, PIPE
from pwn import *
import string

def solve_with_subprocess():
    possibility = string.ascii_letters + string.digits + '_'
    flag = ''
    level = ''
    for i in range(1, 21):
        for j in possibility:
            process = Popen('./nani-the-fuk', stdin = PIPE, stdout = PIPE, stderr = PIPE)
            process.stdout.read(13)
            output = process.stdout.read(14)
            # print output
            if flag != '':
                for x in flag:
                    process.stdin.write(x)
                    process.stdout.read(14)
            process.stdin.write(j)
            level = process.stdout.read(14)
            if ('{}/20'.format(i + 1) in level) or ('hacktoday' in level):
                flag += j
                break
            else:
                process.stdin.close()
                process.terminate()
        print "Level {} : Done".format(i)
    
    print "hacktoday{%s}" % flag

if __name__ == "__main__":
    solve_with_subprocess()