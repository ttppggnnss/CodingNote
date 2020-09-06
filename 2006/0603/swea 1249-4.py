import sys
sys.stdin=open('../input.txt', 'r')

def dijkstra():
    board2[0][0]=0
    q = [(0,0)]
    while q:
        i, j = q.pop(0)
        for ni, nj in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
            if -1<ni<n and -1<nj<n:
                # 값 바뀌면 다시 확인
                if board2[ni][nj]>board2[i][j]+board[ni][nj]:
                    board2[ni][nj] = board2[i][j]+board[ni][nj]
                    q.append((ni,nj))

for t in range(1, int(input())+1):
    n = int(input())
    board = [[*map(int, input())] for _ in range(n)]
    board2 = [[9**9]*n for _ in range(n)]
    dijkstra()
    print('#%i'%t, board2[n-1][n-1])