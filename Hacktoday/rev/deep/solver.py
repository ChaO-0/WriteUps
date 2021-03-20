import string

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

def eulerian(n, m): 
    dp = [[0 for x in range(m+1)]  
             for y in range(n+1)]     
    for i in range(1, n+1): 
        for j in range(0, m+1): 
            if (i > j): 
                if (j == 0): 
                    dp[i][j] = 1
                else : 
                    dp[i][j] = (((i - j) * 
                       dp[i - 1][j - 1]) + 
                       ((j + 1) * dp[i - 1][j]))                       
    return dp[n][m] 
  
n = string.letters + string.digits + '{}_\''
m = 1
flag = ''
for j in range(len(x)):
    for i in n:
        if eulerian(ord(i), m) == x[j]:
            flag += i

print flag