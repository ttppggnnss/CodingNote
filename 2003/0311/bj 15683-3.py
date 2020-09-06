# 실행시간
import sys
sys.stdin=open('input.txt','r')

def f(y,x,direct):
    s=set()
    for d in direct:
        ny,nx=y+dy[d],x+dx[d]
        while -1<ny<n and -1<nx<m and board[ny][nx]!=6:
            if board[ny][nx]<1:
                s.add((ny,nx))
            ny, nx = ny + dy[d], nx + dx[d]
    return s # cctv 가 감시하는 방향에서 0인 좌표

def d(c,v):
    global ccMax
    if c==len(cctv):
        ccMax=max(len(v),ccMax)
        return
    for monitor in cctv[c]:
        d(c+1,v|monitor)

     #상 우 하 좌
dy = [-1,0,1,0]
dx = [0,1,0,-1]
n,m=map(int,input().split())
board = [[*map(int,input().split())]for _ in'a'*n]
U,R,D,L = 0,1,2,3
ans=0
cctv=[]
for y in range(n):
    for x in range(m):
        if board[y][x] == 1:
            cctv.append([f(y,x,[R]),f(y,x,[D]),f(y,x,[L]),f(y,x,[U])]) # 좌표들로 이루어져있다
        if board[y][x] == 2:
            cctv.append([f(y,x,[U,D]),f(y,x,[R,L])])
        if board[y][x] == 3:
            cctv.append([f(y,x,[U,R]),f(y,x,[R,D]),f(y,x,[D,L]),f(y,x,[L,U])])
        if board[y][x] == 4:
            cctv.append([f(y,x,[U,R,D]),f(y,x,[R,D,L]),f(y,x,[D,L,U]),f(y,x,[L,U,R])])
        if board[y][x] == 5:
            cctv.append([f(y,x,[U,D,R,L])])
        if board[y][x]<1:
            ans+=1
ccMax=0
d(0,set())
print(ans-ccMax)