# 시간 초과
import sys
sys.stdin=open('../input.txt', 'r')

from collections import deque

di=[0,0,1,-1]
dj=[1,-1,0,0]
def bfs(i,j):
    q=deque()
    q.append((i,j,1))
    res=0
    while q:
        i,j,k = q.popleft()
        res=max(res,k)
        for z in range(4):
            ni,nj = i+di[z], j+dj[z]
            if -1<ni<n and -1<nj<n and board[ni][nj]>board[i][j]:
                q.append((ni,nj,k+1))
    return res

n = int(input())
board = [[*map(int,input().split())] for _ in range(n)]
ans=0
for i in range(n):
    for j in range(n):
        ans=max(ans,bfs(i,j))
print(ans)

