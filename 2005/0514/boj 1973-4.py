import sys
sys.stdin=open('../input.txt', 'r')
sys.setrecursionlimit(9**9)
input = sys.stdin.readline
def dfs(i, j):
    if board2[i][j]:
        return board2[i][j]
    board2[i][j]=1
    if 0<i and board[i][j]<board[i-1][j]:
        board2[i][j] = max(board2[i][j], dfs(i-1, j)+1)
    if i<n-1 and board[i][j]<board[i+1][j]:
        board2[i][j] = max(board2[i][j], dfs(i+1, j)+1)
    if 0<j and board[i][j]<board[i][j-1]:
        board2[i][j] = max(board2[i][j], dfs(i, j-1)+1)
    if j<n-1 and board[i][j]<board[i][j+1]:
        board2[i][j] = max(board2[i][j], dfs(i, j+1)+1)
    return board2[i][j]

n = int(input())
board = [[*map(int, input().split())] for _ in range(n)]
board2 = [[0]*n for _ in range(n)]
ans=0
for i in range(n):
    for j in range(n):
        ans=max(ans, dfs(i, j))
print(ans)
