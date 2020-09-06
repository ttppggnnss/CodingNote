import sys
sys.stdin=open('../input.txt', 'r')

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
def dijkstra():
    a, b = 0, 0
    board2[0][0]=0
    q = [(a,b,[zz[:] for zz in visit])]
    while q:
        print(q)
        for _ in range(len(q)):
            a, b, V = q.pop(0)
            if (a,b)==(n-1,n-1):
                break
            minn = 9 ** 9
            for z in range(4):
                i, j = a+di[z], b+dj[z]
                if -1<i<n and -1<j<n and V[i][j]<1:
                    if minn<9**9 and minn>=board2[i][j]:
                        q.append((a,b,[zz[:] for zz in V]))
                        minn = board2[i][j]
                        a, b = i, j
            V[a][b] = 1
            for z in range(4):
                ni, nj = a+di[z], b+dj[z]
                if -1<ni<n and -1<nj<n and board2[ni][nj]>board2[a][b]+board[ni][nj]:
                    board2[ni][nj] = board2[a][b]+board[ni][nj]
# for t in range(1, int(input())+1):
input()
for t in range(1, 3):
    n = int(input())
    board = [[*map(int, input())] for _ in range(n)]
    board2 = [[9**9]*n for _ in range(n)]
    visit = [[0] * n for _ in range(n)]
    dijkstra()
    print(board)
    print(board2)
    ans = board2[n-1][n-1]
    print('#%i'%t, ans)