# 오답
import sys
from collections import deque

sys.stdin=open('input.txt','r')

input = sys.stdin.readline
y,x = map(int,input().split())
L=[[*map(int,input().split())] for _ in [0]*y]

def linked(j,i):
    visited[j][i]=1
    q=[(j,i)]
    while q:
        b,a=q.pop()
        for dy,dx in (-1,0),(1,0),(0,1),(0,-1):
            if 0<=a+dx<x and 0<=b+dy<y:
                if L[b+dy][a+dx]>0 and visited[b+dy][a+dx]<1:
                    q.append((b+dy,a+dx))
                    visited[b+dy][a+dx]=1
time=0
while 1:
    time+=1
    for j in range(y):
        for i in range(x):
            if L[j][i]>0:
                L[j][i]-=1
    visited=[[0]*x for _ in [0]*y]
    cnt=0
    for j in range(y):
        for i in range(x):
            if L[j][i]>0 and visited[j][i]<1:
                linked(j,i)
                cnt+=1
    if cnt==0:
        time=0
        break
    elif cnt>1:
        break
print(time)