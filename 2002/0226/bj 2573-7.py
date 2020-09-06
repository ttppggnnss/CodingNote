# 시간초과, 답 틀림
from sys import stdin
stdin=open("input.txt","r")
input = stdin.readline

def bfs(i, j, check):
    bq=[(i,j)]
    check[i][j] = True
    while bq:
        x, y = bq.pop(0)
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0<=nx<n and 0<=ny<m:
                if check[nx][ny]==0 and a[nx][ny] > 0:
                    bq.append((nx, ny))
                    check[nx][ny]=1

n, m = map(int, input().split())
a = [[*map(int, input().split())] for _ in range(n)]
q = []
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

for i in range(n):
    for j in range(m):
        if a[i][j] > 0:
            q.append((i, j))
        else:
            a[i][j] = -1
time=0
while q:
    p=[]
    for _ in range(len(q)):
        x,y=q.pop(0)
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0<=nx<n and 0<=ny<m:
                if a[x][y] > 0 and a[nx][ny] == -1:
                    a[x][y] -= 1
        if a[x][y] > 0:
            q.append((x, y))
        elif a[x][y] == 0:
            p.append((x, y))
    while p:
        x, y = p.pop(0)
        a[x][y] = -1

    time+=1
    cnt=0
    check=[[0]*m for _ in [0]*n]
    for _ in range(len(q)):
        x,y=q.pop(0)
        q.append((x,y))
        if check[x][y]==0:
            bfs(x,y,check)
            cnt+=1
            if cnt>1:
                z=1
    else:
        z=0
    if z:
       break
print(time)