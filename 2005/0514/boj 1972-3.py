# 런타임에러??
# 992ms

import sys
sys.stdin=open('../input.txt', 'r')
sys.setrecursionlimit(9**9)

di=[0, 0, 1, -1]
dj=[1, -1, 0, 0]
def dfs(i, j):
    if board2[i][j]:
        return board2[i][j]
    board2[i][j]=1
    for z in range(4):
        ni, nj = i+di[z], j+dj[z]
        if -1<ni<n and -1<nj<n and board[i][j]<board[ni][nj]:
            board2[i][j]=max(board2[i][j], dfs(ni, nj)+1)
    return board2[i][j]

n = int(input())
board = [[*map(int, input().split())] for _ in range(n)]
board2 = [[0]*n for _ in range(n)]
ans=0
for i in range(n):
    for j in range(n):
        ans=max(ans, dfs(i, j))
        if ans==n**2:break
print(ans)
