import sys
sys.stdin=open('../input.txt', 'r')

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

for t in range(1, int(input())+1):
    n = int(input())
    board = [[*map(int, input())] for _ in range(n)]
    board2 = [[9**9]*n for _ in range(n)]

    board2[0][0] = 0
    board2[n-1][n-1] = 0

    for i in range(1, n):
        board2[i][0] = board2[i-1][0]+board[i][0]
    for j in range(1, n):
        board2[0][j] = board2[0][j-1]+board[0][j]

    for i in range(1, n):
        for j in range(1, n):
            board2[i][j] = min(board2[i-1][j], board2[i][j-1]) + board[i][j]

    ans = board2[n-1][n-1]
    visit = [[0]*n for _ in range(n)]
    visit=set()
    visit.add((0,0))
    q = [(0, 0, 0, visit.copy())]
    zz=0
    while q:
        if zz:
            break
        for _ in range(len(q)):
            i, j, k, V = q.pop()

            if k>=ans: continue
            if i == n-1 and j == n-1:
                ans = k
                zz=1
                break
            for z in range(4):
                ni, nj = i + di[z], j + dj[z]
                if -1<ni<n and -1<nj<n and (ni,nj) not in V:
                    V.add((ni,nj))
                    q.append((ni, nj, k + board[ni][nj], V.copy()))
                    V.remove((ni,nj))
    print('#%i'%t, ans)