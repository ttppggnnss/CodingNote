# 통과
import sys
from collections import deque
sys.stdin=open('input.txt','r')
input=sys.stdin.readline

n,m=map(int,input().split())
L=[[*map(int,input().split())] for _ in 'a'*n]
k=0
q=deque()
V=set()
for i in range(n):
    for j in range(m):
        if L[i][j]>0:
            q.append((i,j))
            V.add((i,j))
            k+=1
time=0
while 1:
    time+=1
    for b in range(k):
        i,j=q.popleft()
        cnt = 0
        if L[i + 1][j] < 1 and (i+1,j) not in V:
            cnt += 1
        if L[i - 1][j] < 1 and (i-1,j) not in V:
            cnt += 1
        if L[i][j + 1] < 1 and (i,j+1) not in V:
            cnt += 1
        if L[i][j - 1] < 1 and (i,j-1) not in V:
            cnt += 1
        L[i][j]-=cnt
        if L[i][j]>0:
            q.append((i,j))
            V.add((i,j))
    if k!=len(q):
        k=len(q)
        if k:
            p=[q[0]]
            V=set()
            while p:
                i,j=p.pop()
                V.add((i,j))
                if L[i+1][j]>0 and (i+1,j) not in V:
                    p.append((i+1,j))
                if L[i-1][j]>0 and (i-1,j) not in V:
                    p.append((i-1,j))
                if L[i][j+1]>0 and (i,j+1) not in V:
                    p.append((i,j+1))
                if L[i][j-1]>0 and (i,j-1) not in V:
                    p.append((i,j-1))
            if k>len(V):
                print(time)
                break
            else:
                continue
        else:
            print(0)
            break

