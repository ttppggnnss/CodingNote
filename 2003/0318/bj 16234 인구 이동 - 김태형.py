import sys
sys.stdin=open("input.txt","r")

N, L, R, = map(int,input().split())
arr = [[i for i in map(int,input().split())] for j in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
unite = []
queue = []
visited = [[0]* N for _ in range(N)]
visited2 = [[0]* N for _ in range(N)]

def BFS():
    global L, R, cnt, visited, k, TF, visited2
    while queue:
        y = queue[0][0]
        x = queue[0][1]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny <= N-1 and 0 <= nx <= N-1 and not visited[ny][nx]:
                queue.append([ny,nx])
                visited[ny][nx] = 1
                if L <= abs(arr[y][x] - arr[ny][nx]) <= R and not visited2[ny][nx]:
                    unite.append([y,x])
                    k += 1
                    TF = True
                    DFS(k)

        queue.pop(0)
        if not queue and TF:
            total = [0] * (k+1)
            length = [0] * (k+1)
            for j in range(1,k+1):
                for m in range(N):
                    for n in range(N):
                        if visited2[m][n] == j:
                            total[j] += arr[m][n]
                            length[j] += 1
            for j in range(1,k+1):
                for m in range(N):
                    for n in range(N):
                        if visited2[m][n] == j:
                            arr[m][n] = total[j]//length[j]      
            queue.append([0,0])
            visited = [[0]* N for _ in range(N)]
            visited2 = [[0]* N for _ in range(N)]
            visited[0][0] = 1
            cnt += 1
            k = 0
            TF = False

def DFS(k):
    while unite:
        y = unite[-1][0]
        x = unite[-1][1]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny <= N-1 and 0 <= nx <= N-1 and L <= abs(arr[y][x] - arr[ny][nx]) <= R and not visited2[ny][nx]:
                unite.append([ny,nx])
                visited2[ny][nx] = k
                break
        else:
            unite.pop()
cnt = 0
k = 0
TF= False
queue.append([0,0])
visited[0][0] = 1
BFS()
print(cnt)