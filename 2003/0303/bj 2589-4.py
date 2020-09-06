# 시간단축
import sys
sys.stdin=open('input.txt','r')
from collections import deque
input=sys.stdin.readline
def dfs(x, y):
    chk = True
    visit[x][y] = 1
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if -1 < tx < N and -1 < ty < M and board[tx][ty] == 'L' and visit[tx][ty] == 0:
            chk = False
            dfs(tx, ty)
    if chk: tmp.append([x, y])

N, M = map(int, input().split())
board = [[*input()] for _ in 'a'*N]
ans=0
tmp = []
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
visit = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        if board[i][j] == 'L' and visit[i][j] == 0:
            tmp.append([i, j])
            dfs(i, j)

for i in tmp:
    visit = [[0 for _ in range(M)] for _ in range(N)]
    tmp2 = deque([i])
    cnt = 0
    while tmp2:
        cnt += 1
        for _ in range(len(tmp2)):
            q = tmp2.popleft()
            x, y = q[0], q[1]
            visit[x][y] = 1
            for j in range(4):
                tx = x + dx[j]
                ty = y + dy[j]
                if -1 < tx < N and -1 < ty < M and board[tx][ty] == 'L' and visit[tx][ty] == 0:
                    visit[tx][ty] = 1
                    tmp2.append([tx, ty])
    ans=max(ans,cnt-1)
print(ans)