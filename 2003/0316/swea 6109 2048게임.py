import sys
sys.stdin=open('input.txt','r')
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
D = {'left': 0, 'right': 1, 'up': 2, 'down': 3}
for t in range(1, int(input()) + 1):
    n, s = input().split();
    n = int(n)
    b = [[*map(int, input().split())] for _ in 'a' * n]
    v = [[0] * n for _ in 'a' * n]
    if s in 'upleft':k=range(n)
    else:k=range(n-1,-1,-1)
    for i in k:
        for j in k:
            if b[i][j] > 0:
                y, x = i, j
                ny, nx = y + dy[D[s]], x + dx[D[s]]
                while 1:
                    if -1 < ny < n and -1 < nx < n:
                        if b[ny][nx] == 0:
                            b[y][x], b[ny][nx] = b[ny][nx], b[y][x]
                        elif b[ny][nx] == b[y][x] and v[ny][nx] < 1:
                            v[ny][nx] = 1
                            b[ny][nx] *= 2
                            b[y][x] = 0
                            break
                        else:
                            break
                        y, x = ny, nx
                        ny, nx = ny + dy[D[s]], nx + dx[D[s]]
                    else:
                        break
    print('#%i' % t)
    for i in b:
        print(*i)

