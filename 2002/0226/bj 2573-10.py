# 풀이 참조

from sys import *

input = stdin.readline
from collections import *


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visit[x][y] = 1
    while q:
        x, y = q.popleft()
        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx > n - 1 or ny > m - 1 or visit[nx][ny] != -1: continue
            if arr[nx][ny] <= 0:
                arr[x][y] -= 1
            else:
                visit[nx][ny] = 1
                q.append((nx, ny))

n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
cnt = 0
while 1:
    f = 0
    visit = [[-1] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0 and visit[i][j] == -1:
                bfs(i, j)
                f += 1
    if f == 0:
        print(0)
        break
    elif f >= 2:
        print(cnt)
        break
    cnt += 1