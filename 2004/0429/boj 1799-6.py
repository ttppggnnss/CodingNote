# 분할 안하면 시간 초과

import sys
sys.stdin=open('../input.txt','r')

def solve(p,z):
    global ans1
    ans1=max(len(p),ans1)
    for z2 in range(z,len(board2)):
        i,j=board2[z2]
        if i-j not in visit1 and i+j not in visit2:
            visit1.append(i-j)
            visit2.append(i+j)
            solve(p+[(i,j)],z2+1)
            visit1.pop()
            visit2.pop()

n=int(input())
board=[]
board2=[]

visit1=[]
visit2=[]

for i in range(n):
    board.append([*map(int,input().split())])
    for j in range(n):
        if board[i][j]==1:board2.append((i,j))

ans1=0
solve([],0)
print(ans1)