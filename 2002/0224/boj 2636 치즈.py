# https://www.acmicpc.net/problem/2636

import sys
sys.stdin=open('input.txt','r')

y, x = map(int,input().split())
L=[[*map(int,input().split())] for _ in [0]*y]

time=0
cnt=0
while 1:
    nxt=[]
    q=[(0,0)]
    while q:
        x0,y0=q.pop()
        for dx,dy in (1,0),(-1,0),(0,1),(0,-1):
            nx,ny =x0+dx,y0+dy
            if 0<=nx<x and 0<=ny<y:
                if L[ny][nx]==0:
                    L[ny][nx]=-1
                    q.append((nx,ny))
                if L[ny][nx]==1:
                    L[ny][nx]=-1
                    nxt.append((nx,ny))
        print()
        for i in L:
            print(*i)
    if not nxt:
        break
    time+=1
    cnt=len(nxt)
    for i in range(x):
        for j in range(y):
            if L[j][i]==-1:
                L[j][i]=0
print(time,cnt,sep='\n')