import sys
sys.stdin=open('../input.txt', 'r')

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
import heapq

def dijkstra():
    board2[0][0]=0
    q = []
    heapq.heappush(q, (0,0))
    visit[0][0]=1
    while q:
        # 현재 위치
        i, j = heapq.heappop(q)
        # 갈 수 있는 곳들 (사방위)
        for z in range(4):
            ni, nj = i+di[z], j+dj[z]
            if -1<ni<n and -1<nj<n:
                # 방문안했거나 방문했어도 값이 작으면
                if visit[ni][nj]<1 or board2[ni][nj]>board2[i][j]+board[ni][nj]:
                    board2[ni][nj] = board2[i][j]+board[ni][nj]
                    heapq.heappush(q, (ni,nj))
                    visit[ni][nj]=1

for t in range(1, int(input())+1):
    n = int(input())
    board = [[*map(int, input())] for _ in range(n)]
    board2 = [[9**9]*n for _ in range(n)]
    visit = [[0]*n for _ in range(n)]
    dijkstra()
    ans = board2[n-1][n-1]
    print('#%i'%t, ans)