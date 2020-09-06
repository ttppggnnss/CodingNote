import sys
from collections import deque
import itertools

input = sys.stdin.readline

EMPTY, GREEN, RED, FLOWER = 0, 1, 2, 3
n, m, g, r = 0, 0, 0, 0
board = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

cand = []  # 좌표를 담을 에정
candsz = 0
chosen_g = [0] * 5
chosen_r = [0] * 5
mx = 0


# popleft, append
def solve():
    cnt = 0
    state = [[[0] * 2 for i in range(m)] for j in range(n)]
    q = deque()

    for i in range(g):
        state[cand[chosen_g[i]][0]][cand[chosen_g[i]][1]] = [0, GREEN]
        q.append(cand[chosen_g[i]])

    for i in range(r):
        state[cand[chosen_r[i]][0]][cand[chosen_r[i]][1]] = [0, RED]
        q.append(cand[chosen_r[i]])

    while q:
        cur = q.popleft()
        curtime, curcolor = state[cur[0]][cur[1]]
        if state[cur[0]][cur[1]][1] == FLOWER: continue
        for dir in range(4):
            nx = cur[0] + dx[dir]
            ny = cur[1] + dy[dir]
            if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
            if board[nx][ny] == 0: continue
            if state[nx][ny][1] == EMPTY:
                state[nx][ny] = [curtime + 1, curcolor]
                q.append([nx, ny])
            elif state[nx][ny][1] == RED:
                if curcolor == GREEN and state[nx][ny][0] == curtime + 1:
                    cnt += 1
                    state[nx][ny][1] = FLOWER
            elif state[nx][ny][1] == GREEN:
                if curcolor == RED and state[nx][ny][0] == curtime + 1:
                    cnt += 1
                    state[nx][ny][1] = FLOWER
    return cnt


n, m, g, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            cand.append([i, j])
candsz = len(cand)

for c1 in itertools.combinations(range(candsz), g + r):
    for c2 in itertools.combinations(range(g + r), g):
        ridx, gidx = 0, 0
        for i in range(g + r):
            if i in c2:
                chosen_g[gidx] = c1[i]
                gidx += 1
            else:
                chosen_r[ridx] = c1[i]
                ridx += 1
        mx = max(mx, solve())

sys.stdout.write(str(mx) + "\n")