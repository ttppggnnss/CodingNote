# 통과
import sys
sys.stdin=open('input.txt', 'r')
input=sys.stdin.readline
from collections import deque

def bfs(S,cnt=-1):
    p=deque([S])
    V={S}
    while p:
        for k in range(len(p)):
            i,j=p.popleft()
            for di,dj in (1,0),(-1,0),(0,1),(0,-1):
                ni,nj=i+di,j+dj
                if 0<=ni<y and 0<=nj<x and M[ni][nj]=='L' and (ni,nj) not in V:
                    p.append((ni,nj))
                    V.add((ni,nj))
        cnt+=1
    return cnt

y,x =map(int,input().split())
M=[[*input()] for _ in'a'*y]
ans=[]
for i in range(y):
    for j in range(x):
        if M[i][j]=='L':
            ans.append(bfs((i,j)))
print(max(ans))