# 빙산 DFS
import sys
sys.stdin=open('input.txt','r')

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def DFS2(y,x):
    global N,M, icebergs
    visited=set()
    icebergs.add((y,x))
    stack=[(y,x)]
    visited.add((y,x))
    while stack:
        vy,vx=stack.pop()
        for i in range(4):
            ny = vy + dy[i]
            nx = vx + dx[i]
            if 0 <= ny < N and 0 <= nx < M and (ny,nx) not in visited and (ny,nx) in icebergs:
                visited.add((ny,nx))
                stack.append((ny,nx))
    return len(visited)

def DFS(y, x):
    global N, M, icebergs
    visited=set()
    icebergs.add((y,x))
    stack = [(y,x)]
    visited.add((y,x))
    tempcnt = 0
    if y + 1 < N and field[y+1][x] <1: tempcnt += 1
    if x + 1 < M and field[y][x+1] <1: tempcnt += 1
    if 0 <= y - 1 and field[y-1][x] <1: tempcnt += 1
    if 0 <= x - 1 and field[y][x-1] <1: tempcnt += 1
    melts.append((y, x, tempcnt))

    while stack:
        vy, vx = stack.pop()

        for i in range(4):
            ny = vy + dy[i]
            nx = vx + dx[i]

            if 0 <= ny < N and 0 <= nx < M and (ny,nx) not in visited and field[ny][nx] > 0:
                visited.add((ny,nx))
                stack.append((ny,nx))
                tempcnt = 0
                if ny + 1 < N and field[ny+1][nx] <1: tempcnt += 1
                if nx + 1 < M and field[ny][nx+1] <1: tempcnt += 1
                if 0 <= ny - 1 and field[ny-1][nx] <1: tempcnt += 1
                if 0 <= nx - 1 and field[ny][nx-1] <1: tempcnt += 1
                melts.append((ny, nx, tempcnt))

N, M = map(int, input().split())
field = [list(map(int, input().split())) for j in range(N)]
result = 0
icebergs = set()

for i in range(N):
    for j in range(M):
        if field[i][j] > 0:
            icebergs.add((i,j))
while icebergs:
    result+=1
    melts = []
    DFS(*icebergs.pop())
    for i in range(len(melts)):
        y, x, count = melts[i]
        field[y][x] -= count
        if field[y][x] <1:icebergs-={(y,x)}
    if not icebergs:
        result=0
        break
    if len(icebergs)!=DFS2(*icebergs.pop()):
        break
print(result)