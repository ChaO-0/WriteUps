from z3 import *

def solve():
    x =[Int(str(i)) for i in range(25)]
    s = Solver()

    s.add(x[20] - x[0] == 24)

    s.add(x[8] + x[5] == 126)
    
    s.add(x[14] * x[5] == 3696)
    
    s.add(x[21] - x[1] == 33)
    
    s.add( x[10] - x[0] == 2 )
    
    s.add( x[17] - x[0] == 19 )     
    
    s.add( x[17] * x[1] == 3848 )   
    
    s.add( x[4] + x[6] == 123 ) 
    
    s.add( x[13] * x[16] == 4488 )  
    
    s.add( x[1] * x[6] == 2600 )
    
    s.add( x[13] * x[23] == 3536 )
    
    s.add( x[8] - x[5] == 14 )
    
    s.add( x[15] + x[5] == 123 )
    
    s.add( x[20] - x[17] == 5 )
    
    s.add( x[17] + x[16] == 140 )
    
    s.add( x[16] + x[14] == 132 )
    
    s.add( x[3] * x[6] == 4250 )
    
    s.add( x[18] + x[14] == 145 )
    
    s.add( 2 * x[13] == 136 )
    
    s.add( x[17] - x[10] == 17 )
    
    s.add( x[11] + x[8] == 145 )
    
    s.add( x[9] + x[1] == 135 )
    
    s.add( x[11] + x[24] == 146 )
    
    s.add( x[3] - x[7] == 11 )
    
    s.add( x[0] - x[2] == 2 )
    
    s.add( x[11] - x[13] == 7 )
    
    s.add( x[3] + x[4] == 158 )
    
    s.add( x[3] - x[16] == 19 )
    
    s.add( x[4] - x[14] == 7 )
    
    s.add( x[12] * x[1] == 4056 )
    
    s.add( x[20] + x[8] == 149 )
    
    s.add( x[9] - x[4] == 10 )
    
    s.add( x[9] - x[6] == 33 )
    
    s.add( x[9] * x[13] == 5644 )
    
    s.add( x[16] + x[5] == 122 )
    
    s.add( x[16] - x[10] == 9 )
    
    s.add( x[17] + x[24] == 145 )
    
    s.add( x[20] - x[13] == 11 )
    
    s.add( x[18] * x[11] == 5925 )
    
    s.add( x[21] * x[23] == 4420 )
    
    s.add( x[22] * x[7] == 5698 )
    
    s.add( x[15] - x[19] == 12 )
    
    s.add( x[16] - x[1] == 14 )
    
    s.add( x[3] - x[13] == 17 )
    
    s.add( x[12] * x[8] == 5460 )
    
    s.add( x[21] * x[13] == 5780 )
    
    s.add( x[7] * x[1] == 3848 )
    
    s.add( x[22] + x[6] == 127 )
    
    s.add( x[13] + x[5] == 124 )

    # s.add( x[24] + x[1] == 123 )

    for i in range(len(x)):
        s.add(x[i] >= 26)
        s.add(x[i] <= 0xff)

    w = {5 : 56,
        21 : 85,
        3 : 85,
        19 : 55,
        22 : 77,
        23 : 52,
        18 : 79,
        20 : 79,
        16 : 66,
        9 : 83,
        6 : 50,
        4 : 73,
        8 : 70,
        12 : 78,
        14 : 66,
        11 : 75,
        2 : 53,
        7 : 74,
        24 : 71,
        13 : 68,
        17 : 74,
        15 : 67,
        10 : 57,
        1 : 52,
        0 : 55}

    s.check()
    sv = s.model()
    print sv

    key = []
    for i in range(25):
        key.append(chr(w[i]))
    
    test = ''.join(key[:5]) , "-" , ''.join(key[5:10]) , "-" , ''.join(key[10:15]) , "-" , ''.join(key[15:20]) , "-" , ''.join(key[20:25])
    print ''.join(test)
    # print key[6:11]
    print len(key)

if __name__ == "__main__":
    solve()