# 4875 미로

import sys
sys.stdin=open("input3.txt","r")

def maze(x,y):
    if L[y][x]=='3':
        global ans
        ans=1
        return
    elif L[y][x]!='1':
        L[y][x]='1'
        for dx, dy in (1, 0), (-1, 0), (0, 1),(0,-1):
            if 0 <= x + dx < N and 0 <= y + dy < N:
                nx, ny = x + dx, y + dy
                maze(nx,ny)
    elif L[y][x]=='1':
        return
for t in range(1,int(input())+1):
    ans=0
    N=int(input())
    L=[list(input()) for _ in [0]*N]
    for i in range(N):
        if'2'in L[i]:
            y=i
            x=L[i].index('2')
    maze(x,y)
    print('#%i'%t,ans)


