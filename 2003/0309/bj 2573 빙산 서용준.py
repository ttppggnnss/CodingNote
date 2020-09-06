# 빙산 DFS
import sys
sys.stdin=open('input.txt','r')

def DFS(y, x):
    global N, M, icebergs
    visited = [[0 for i in range(M)] for j in range(N)]
    stack = [(y,x)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    visited[y][x] = 1
    tempcnt = 0
    if y + 1 < N and field[y+1][x] < 1: tempcnt += 1
    if x + 1 < M and field[y][x+1] < 1: tempcnt += 1
    if 0 <= y - 1 and field[y-1][x] < 1: tempcnt += 1
    if 0 <= x - 1 and field[y][x-1] < 1: tempcnt += 1
    melts.append((y, x, tempcnt))

    while stack:
        vy, vx = stack.pop()

        for i in range(4):
            ny = vy + dy[i]
            nx = vx + dx[i]

            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and field[ny][nx] > 0:
                visited[ny][nx] = 1
                stack.append((ny,nx))
                icebergs = icebergs -{(ny,nx)}
                tempcnt = 0
                if ny + 1 < N and field[ny+1][nx] < 1: tempcnt += 1
                if nx + 1 < M and field[ny][nx+1] < 1: tempcnt += 1
                if 0 <= ny - 1 and field[ny-1][nx] < 1: tempcnt += 1
                if 0 <= nx - 1 and field[ny][nx-1] < 1: tempcnt += 1
                melts.append((ny, nx, tempcnt))

N, M = map(int, input().split())
field = [list(map(int, input().split())) for j in range(N)]
result = 0

while True:
    icebergs = set()
    melts = []
    found = True
    for i in range(N):
        for j in range(M):
            if field[i][j] > 0:
                icebergs.add((i,j))
    else:
        found = False
    if found:
        result = 0
        break

    DFS(*icebergs.pop())
    if icebergs: break

    for i in range(len(melts)):
        y, x, count = melts[i]
        field[y][x] -= count

    result += 1

print(result)