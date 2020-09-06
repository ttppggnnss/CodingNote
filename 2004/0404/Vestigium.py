# 7점 획득

# 3
# 4
# 1 2 3 4
# 2 1 4 3
# 3 4 1 2
# 4 3 2 1
# 4
# 2 2 2 2
# 2 3 2 3
# 2 2 2 3
# 2 2 2 2
# 3
# 2 1 3
# 1 3 2
# 1 2 3

import sys
sys.stdin=open('../input.txt','r')

for t in range(1,int(input())+1):
    n=int(input())
    board=[[*map(int,input().split())]for _ in range(n)]
    k=r=c=0
    for i in range(n):
        k+=board[i][i]
    for i in board:
        for j in range(1,n+1):
            if i.count(j)>1:
                r+=1
                break
    board2=list(zip(*board))
    for i in board2:
        for j in range(1,n+1):
            if i.count(j)>1:
                c+=1
                break
    print('Case #%i:'%t,k,r,c)