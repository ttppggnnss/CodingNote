from sys import stdin
from collections import deque
input = stdin.readline

y, x = map(int,input().split())
arr = []
cnt = 0
L=[[*map(int,input().split())] for _ in [0]*y]
for i in L:
    for j in i:
        if j:
            cnt += 1
new_cnt = cnt

def bfs(i, j):
    global new_cnt
    visited = {(i, j)}
    q = deque([(i, j)])
    while q:
        i, j = q.popleft()
        for di, dj in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            if not (0 <= i+di < y and 0 <= j+dj < x):
                continue
            if not L[i + di][j + dj] and (i+di, j+dj) not in visited:
                if L[i][j]:
                    L[i][j] -= 1
                    if not L[i][j]:
                        new_cnt -= 1
            elif (i+di, j+dj) not in visited:
                visited.add((i+di, j+dj))
                q.append((i+di, j+dj))
    return len(visited)

def run():
    for i in range(y):
        for j in range(x):
            if L[i][j]:
                if cnt != bfs(i, j):
                    return True
                return False
    else:
        print(0)
        exit()

time = 0
while not run():
    cnt = new_cnt
    time += 1
print(time)