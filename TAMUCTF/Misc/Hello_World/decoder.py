flag = '''push103
push 105
push 103
push 101
push 109
push 123
push 48
push 104
push 95
push 109
push 121
push 95
push 119
push 104
push 52
push 116
push 95
push 115
push 112
push 52
push 99
push 49
push 110
push 103
push 95
push 121
push 48
push 117
push 95
push 104
push 52
push 118
push 51
push 125
push 33
push 101
push 99
push 97
push 112
push 115
push 101
push 116
push 105
push 104
push 119
push 32
push 102
push 111
push 32
push 116
push 111
push 108
push 32
push 97
push 32
push 115
push 105
push 32
push 101
push 114
push 117
push 115
push 32
push 116
push 97
push 104
push 116
push 32
push 44
push 101
push 101
push 103
push 32
push 121
push 108
push 108
push 111
push 103
push 32
push 116
push 101
push 101
push 119
push 115
push 32
push 108
push 108
push 101
push 87
'''
newflag = ""
flag = flag.replace('push', '')
flag = flag.replace('\n', '')
flag = flag.split(" ")
flag = map(int, flag)

for i in flag:
	newflag += chr(i)
print newflag
