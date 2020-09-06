# 시간 초과
import sys
from collections import deque
sys.stdin=open('input.txt','r')
input=sys.stdin.readline
def cnt0(i,j):
    cnt=0
    if L[i+1][j]<1 and r[i+1][j]<1:
            cnt+=1
    if L[i-1][j]<1 and r[i-1][j]<1:
            cnt+=1
    if L[i][j+1]<1 and r[i][j+1]<1:
            cnt+=1
    if L[i][j-1]<1 and r[i][j-1]<1:
            cnt+=1
    return cnt

n,m=map(int,input().split())
L=[[*map(int,input().split())] for _ in 'a'*n]
k=0
q=deque()
for i in range(n):
    for j in range(n):
        if L[i][j]>0:
            q.append((i,j))
            k+=1
time=0
while 1:
    time+=1
    r=[[0]*m for _ in'a'*n]
    for b in range(k):
        i,j=q.popleft()
        if L[i][j]>0:
            L[i][j]-=cnt0(i,j)
            if L[i][j]<1:
                r[i][j]=1
            else:
                q.append((i,j))
    if k!=len(q):
        k=len(q)
        z=[i for i in q]
        if z:
            p=[z.pop()]
            while p:
                y,x=p.pop()
                if (y+1,x) in z:
                    z.remove((y+1,x))
                    p.append((y+1,x))
                if (y-1,x) in z:
                    z.remove((y-1,x))
                    p.append((y-1,x))
                if (y,x+1) in z:
                    z.remove((y,x+1))
                    p.append((y,x+1))
                if (y,x-1) in z:
                    z.remove((y,x-1))
                    p.append((y,x-1))
        else:
            print(0)
            break
        if z:
            print(time)
            break
