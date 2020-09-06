# if 4번 대신 for 로
# 시간초과
import sys
from collections import deque
sys.stdin=open('input.txt','r')
input=sys.stdin.readline

di=[1,-1,0,0]
dj=[0,0,1,-1]
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
        for z in range(4):
            if L[i+di[z]][j+dj[z]]<1 and (i+di[z],j+dj[z]) not in V:
                L[i][j]-=1
        if L[i][j]>0:
            q.append((i,j))
    if k!=len(q):
        k=len(q)
        if k:
            p=[q[0]]
            V=set()
            while p:
                i,j=p.pop()
                V.add((i,j))
                for z in range(4):
                    if L[i+di[z]][j+dj[z]]>0 and (i+di[z],j+dj[z]) not in V:
                        p.append((i+di[z],j+dj[z]))
            if k>len(V):
                print(time)
                break
        else:
            print(0)
            break

