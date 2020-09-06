# 틀렸습니다?
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
    for j in range(m):
        if L[i][j]>0:
            q.append((i,j))
            k+=1
time=0
while 1:
    time+=1
    r=[[0]*m for _ in'a'*n]
    for b in range(k):
        i,j=q.popleft()
        L[i][j]-=cnt0(i,j)
        if L[i][j]<1:
            r[i][j]=1
        else:
            q.append((i,j))
    if k!=len(q):
        k=len(q)
        if k:
            p=[q[0]]
            k2=0
            while p:
                i,j=p.pop()
                r[i][j]=1
                k2+=1
                if L[i+1][j]>0 and r[i+1][j]<1:
                    p.append((i+1,j))
                if L[i-1][j]>0 and r[i-1][j]<1:
                    p.append((i-1,j))
                if L[i][j+1]>0 and r[i][j+1]<1:
                    p.append((i,j+1))
                if L[i][j-1]>0 and r[i][j-1]<1:
                    p.append((i,j-1))
            if k>k2:
                print(time)
                break
        else:
            print(0)
            break

