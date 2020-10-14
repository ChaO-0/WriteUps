from pwn import *
# Python3 code to find minimum steps to reach  
# to specific cell in minimum moves by Knight  
class cell: 
      
    def init(self, x = 0, y = 0, dist = 0): 
        self.x = x 
        self.y = y 
        self.dist = dist 
          
# checks whether given position is  
# inside the board 
def isInside(x, y, N): 
    if (x >= 1 and x <= N[0] and 
        y >= 1 and y <= N[1]):
        return True
    return False
      
# Method returns minimum step to reach 
# target position  
def minStepToReachTarget(knightpos,  
                         targetpos, N): 
      
    # all possible movments for the knight 
    dx = [2, 2, -2, -2, 1, 1, -1, -1] 
    dy = [1, -1, 1, -1, 2, -2, 2, -2] 
      
    queue = [] 
      
    # push starting position of knight 
    # with 0 distance 
    queue.append(cell(knightpos[0], knightpos[1], 0)) 
      
    # make all cell unvisited  
    visited = [[False for i in range(N[0] + 1)]  
                      for j in range(N[1] + 1)] 
      
    # visit starting state 
    visited[knightpos[0]][knightpos[1]] = True
      
    # loop untill we have one element in queue  
    while(len(queue) > 0): 
          
        t = queue[0] 
        queue.pop(0) 
          
        # if current cell is equal to target  
        # cell, return its distance  
        if(t.x == targetpos[0] and 
           t.y == targetpos[1]): 
            return t.dist 
              
        # iterate for all reachable states  
        for i in range(8): 
              
            x = t.x + dx[i] 
            y = t.y + dy[i] 
              
            if(isInside(x, y, N) and not visited[x][y]): 
                visited[x][y] = True
                queue.append(cell(x, y, t.dist + 1)) 

def solve(board):
    KPOS = []
    TPOS = []
    x = 0
    y = 0
    z = len(board[-2][:-1])//2
    for i in board:
        if '-' not in i:
            y += 1
            tmp = i.replace('|', '')
            for j in tmp:
                x += 1
                if j == 'K':
                    KPOS.append([x, y])
                if j == 'X':
                    TPOS = [x, y]
            x = 0
    pos = [123456789]
    for x in KPOS:
        try:
            # if z > 9 or y > 9:
            #     if x[0] >= z-3 and x[0] <= z+3 and y[1] <= z+5:
            #         pos.append(minStepToReachTarget(x, TPOS, [z, y]))
            # else:
            #     pos.append(minStepToReachTarget(x, TPOS, [z, y]))
            # return x
            pos.append(minStepToReachTarget(x, TPOS, [z, y]))
        except:
            pass
    return min(pos)

# Driver Code      
if __name__=='__main__':  
    # N = 30
    # knightpos = [1, 1] 
    # targetpos = [30, 30] 
    # print(minStepToReachTarget(knightpos, 
    #                            targetpos, N)) 
      
# This code is contributed by  
# Kaustav kumar Chanda 
    while True:
        r = remote('128.199.157.172', 27136)
        for i in range(8):
            print(i)
            if i == 7:
                print(r.recv())
                exit()
            else:
                try:
                    tmp = r.recvuntil("Your guess: ")
                    print(tmp.decode())
                    board = tmp.decode().split('\n')[1:-1]
                    if "You're not the chess grandmaster" not in board:
                        step = solve(board)
                        if step != 123456789:
                            print(step)
                            r.sendline(str(step))
                        else:
                            print(tmp.decode())
                            print("Can't Solved")
                            break
                    else:
                        print(tmp.decode())
                except:
                    pass
        r.close() 
