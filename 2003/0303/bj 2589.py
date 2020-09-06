# 시간초과
import sys
sys.stdin=open('input.txt','r')
input=sys.stdin.readline
from collections import deque

D=(1,0),(-1,0),(0,1),(0,-1)
def check(s):
    cnt=0
    i,j=s
    for di,dj in D:
        ni,nj=i+di,j+dj
        if 0<=ni<y and 0<=nj<x:
            if M[ni][nj]=='L':
                cnt+=1
    if cnt<=2:
        return True
    else:
        return False
def check2(S,G,cnt=0):
    p=deque([S])
    while p:
        for k in range(len(p)):
            i,j=p.popleft()
            if (i,j)==G:
                return cnt
            V[i][j] = 1
            for di, dj in D:
                ni, nj = i + di, j + dj
                if 0 <= ni < y and 0 <= nj < x:
                    if M[ni][nj] == 'L' and V[ni][nj] < 1:
                        p.append((ni,nj))
        cnt+=1
    return 0

y,x = map(int,input().split())
M=[[*input()] for _ in'a'*y]
L=[]
for i in range(y):
    for j in range(x):
        if M[i][j]=='L':
            if check((i,j)):
                L.append((i,j))
ans=0
r=len(L)
for a in range(r-1):
    for b in range(a+1,r):
        V = [[0] * x for _ in 'a' * y]
        ans=max(ans,check2(L[a],L[b]))
print(ans)