# 시간초과, 틀림

import sys
sys.stdin=open('input.txt','r')
input=sys.stdin.readline
from collections import deque

def linked(y0,x0):
    q=deque()
    q.append((y0,x0))
    V[y0][x0]=1
    L[y0][x0]-=1
    while q:
        y1,x1=q.popleft()
        for dx,dy in (0,1),(0,-1),(1,0),(-1,0):
            nx,ny=x1+dx,y1+dy
            if 0<=nx<x and 0<=ny<y:
                if L[ny][nx]>0 and V[ny][nx]<1:
                    L[ny][nx]-=1
                    V[ny][nx]=1
                    q.append((ny,nx))

y, x = map(int,input().split())
L=[[*map(int,input().split())] for _ in[0]*y]
time=0
while 1:
    cnt=0
    V=[[0]*x for _ in [0]*y]
    for i in range(y):
        for j in range(x):
            if L[i][j]>0 and V[i][j]<1:
                linked(i,j)
                cnt+=1
            if cnt>1:
                break
        if cnt>1:
            break
    if cnt==0:
        print(time)
        break
    elif cnt>1:
        print(time)
        break
    time+=1

