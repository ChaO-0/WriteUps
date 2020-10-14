# uncompyle6 version 3.6.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.17 (default, Apr 15 2020, 17:20:14) 
# [GCC 7.5.0]
# Embedded file name: <script>
x = [20282409603651670423947251285911L, 158456325028528675187087900574L, 633825300114114700748351602588L, 
    162259276829213363391578010288020L, 83076749736557242056487941267521419L, 2596148429267413814265248164609936L,
    1267650600228229401496703205275L, 158456325028528675187087900574L, 2658455991569831745807614120560689030L,
    10633823966279326983230456482242756484L, 664613997892457936451903530140172168L, 20282409603651670423947251285911L, 
    158456325028528675187087900574L, 83076749736557242056487941267521419L, 41538374868278621028243970633760652L, 549755813848, 
    166153499473114484112975882535042954L, 5192296858534827628530496329219983L, 39614081257132168796771975072L, 
    1267650600228229401496703205275L, 
    2596148429267413814265248164609936L, 664613997892457936451903530140172168L, 
    1298074214633706907132624082304913L, 39614081257132168796771975072L, 83076749736557242056487941267521419L, 
    20282409603651670423947251285911L, 2535301200456458802993406410650L, 20769187434139310514121985316880269L, 
    2535301200456458802993406410650L, 39614081257132168796771975072L, 18014398509481929, 5070602400912917605986812821401L, 
    1125899906842573, 36028797018963912, 5070602400912917605986812821401L, 9007199254740938, 2251799813685196, 
    9007199254740938, 42535295865117307932921825928971026306L]
# v = --- This code section failed: ---

#    3         0  LOAD_FAST             1  'y'
#              3  LOAD_CONST               0
#              6  COMPARE_OP            2  ==
#              9  POP_JUMP_IF_TRUE     24  'to 24'
#             12  LOAD_FAST             1  'y'
#             15  LOAD_FAST             0  'x'
#             18  COMPARE_OP            2  ==
#           21_0  COME_FROM             9  '9'
#             21  POP_JUMP_IF_FALSE    28  'to 28'
#             24  LOAD_CONST               1
#             27  RETURN_VALUE_LAMBDA
#           28_0  COME_FROM            21  '21'
#             28  LOAD_GLOBAL           0  'v'
#             31  LOAD_FAST             0  'x'
#             34  LOAD_CONST               1
#             37  BINARY_SUBTRACT  
#             38  LOAD_FAST             1  'y'
#             41  LOAD_CONST               1
#             44  BINARY_SUBTRACT  
#             45  CALL_FUNCTION_2       2  None
#             48  LOAD_GLOBAL           0  'v'
#             51  LOAD_FAST             0  'x'
#             54  LOAD_CONST               1
#             57  BINARY_SUBTRACT  
#             58  LOAD_FAST             1  'y'
#             61  CALL_FUNCTION_2       2  None
#             64  BINARY_ADD       
#             65  RETURN_VALUE_LAMBDA
#             -1  LAMBDA_MARKER   
#             def bruh(x, y):
#               if ((y == 0) or (y == x)):
#                     return 1
#               else:
#                     bruh(x - 1, y - 1) + bruh(x - 1, y)
#             v = lambda x, y: 1 if ((y == 0) or (y == x)) else (v(x -  1, y - 1) + v(x - 1, y))
v = lambda x, y: 1 if ((y == 0) or (y == x)) else (v(x -  1, y - 1) + v(x - 1, y))
y = lambda x: sum([ v(y, w) for y in range(ord(x)) for w in range(y) ])

print y('a')

# z = raw_input('Check flag anda disini :')
# u = [ y(i) for i in str(z) ]

# w = lambda x, y: 'Selamat yang anda input benar' if x == y else 'Flag yang anda input salah'
# print w(u, x)