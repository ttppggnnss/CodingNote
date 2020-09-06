import sys
input = sys.stdin.readline
n,m = map(int,input().split())
board = [list(input().strip()) for _ in range(n)]
check = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

rx,ry,bx,by = [0] * 4
for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            rx,ry = i,j
        elif board[i][j] == 'B':
            bx,by = i,j
idx = [(rx,ry,bx,by,0)]
check[rx][ry][bx][by] = True

def move(x,y,i,j,c):
    c = 0
    while board[x+i][y+j] != '#' and board[x][y] != 'O':
        x += i
        y += j
        c += 1
    return x,y,c

def solution():
    while idx:
        rx,ry,bx,by,count = idx.pop(0)
        if count >= 10:
            break
        for i,j in [(-1,0),(1,0),(0,-1),(0,1)]:
            nrx,nry,rc = move(rx,ry,i,j,0)
            nbx,nby,bc = move(bx,by,i,j,0)
            if board[nbx][nby] == 'O':
                continue
            if board[nrx][nry] == 'O':
                print(count+1)
                return
            if nrx==nbx and nry==nby:
                if rc > bc:
                    nrx -= i
                    nry -= j
                else:
                    nbx -= i
                    nby -= j
            if not check[nrx][nry][nbx][nby]:
                check[nrx][nry][nbx][nby] = True
                idx.append((nrx,nry,nbx,nby,count+1))
    print(-1)
solution()