import sys
sys.stdin=open('input.txt','r')
from collections import deque

def bfs(s):
    p[s]=1
    q=deque([s])
    while q:
        r=0
        for i in range(len(q)):
            a=q.popleft()
            r=max(r,a)
            for j in range(v):  
                if V[a][j]==1 and not p[j]:
                    q.append(j)
                    p[j]=1
    return r

u=input
for t in range(1,11):
    v,s=map(int,u().split())
    V=[[0]*v for _ in 'a'*v]
    L=[*map(int,u().split())]
    p=[0]*(v+1)
    for i in range(len(L)//2):
        b=L.pop()
        a=L.pop()
        V[a][b]=1
    print('#%i'%t,bfs(s))