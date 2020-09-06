import sys
sys.stdin = open('../input.txt','r')

di=[1,-1,0,0]
dj=[0,0,1,-1]
def bfs(start):
    visit=[[0]*n for _ in range(n)]
    cnt=0
    i,j=start[0]
    visit[i][j]=1
    while start:
        for k in 'a'*len(start):
            i,j=start.pop(0)
            for z in range(4):
                ni,nj=i+di[z],j+dj[z]
                if -1<ni<n and -1<nj<n and maze[ni][nj]=='0' and visit[ni][nj]<1:
                    visit[ni][nj]=1
                    start.append((ni,nj))
                if -1<ni<n and -1<nj<n and maze[ni][nj]=='3':
                    return cnt
        cnt+=1
    return 0

for t in range(1, int(input())+1):
    n=int(input())
    maze = []
    for i in range(n):
        maze.append([*input()])
        for j in range(n):
            if maze[i][j]=='2':start=[(i,j)]
    print('#%i'%t,bfs(start))