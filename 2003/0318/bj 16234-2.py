# python3 시간초과
import sys
sys.stdin=open("input.txt","r")
from collections import deque
dy=[0,0,1,-1]
dx=[1,-1,0,0]
def bfs_group(i,j,v1):
    global l, r
    group=[(i,j)]
    q=deque([(i,j)])
    v1[i][j]=1
    groupSum=board[i][j]
    while q:
        for k in'a'*len(q):
            y,x=q.popleft()
            for d in range(4):
                ny,nx=y+dy[d],x+dx[d]
                if -1<ny<n and -1<nx<n and v1[ny][nx]<1 and l<=abs(board[y][x]-board[ny][nx])<=r:
                    v1[ny][nx]=1
                    q.append((ny,nx))
                    group.append((ny,nx))
                    groupSum+=board[ny][nx]
    for g in group:
        board[g[0]][g[1]]=groupSum//len(group)
    if len(group)==1:return 0
    else:return 1
n,l,r=map(int,input().split())
board=[[*map(int,input().split())]for _ in'a'*n]
cnt=0
while 1:
    check=[i[:]for i in board]
    v1 = [[0] * n for _ in 'a' * n]
    for i in range(n):
        for j in range(n):
            if v1[i][j]<1:
                bfs_group(i,j,v1)
    if board==check:
        break
    else:cnt+=1
print(cnt)
# for i in board:
#     print(*i)

