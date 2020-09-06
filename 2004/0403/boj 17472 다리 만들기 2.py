# 가로 두개 연속 있는 다리가 세로로 연결된 다리처럼 생각된다.

import sys
sys.stdin = open('../input.txt','r')

from itertools import combinations as c

di=[0,0,1,-1]
dj=[1,-1,0,0]
def check(j):
    cnt=0
    for a,b in j:
        for i in a:
            board3[i[0]][i[1]]=2
        cnt+=b
    return cnt

def isone(i,j):
    global cnt
    cnt+=1
    visit[i][j]=1
    q=[(i,j)]
    while q:
        i,j=q.pop()
        for k in range(4):
            ni,nj=i+di[k],j+dj[k]
            if -1<ni<n and -1<nj<m and board3[ni][nj]==1 and visit[ni][nj]<1:
                visit[ni][nj]=1
                q.append((ni,nj))
            if -1<ni<n and -1<nj<m and board3[ni][nj]>1 and visit[ni][nj]<1:
                cnt2=1
                while -1<ni<n and -1<nj<m and board3[ni][nj]>1:
                    ni+=di[k]
                    nj+=dj[k]
                    cnt2+=1
                if -1<ni<n and -1<nj<m and board3[ni][nj]==1 and visit[ni][nj]<1 and cnt2>1:
                    visit[ni][nj]=1
                    q.append((ni,nj))

n, m = map(int,input().split())
board = [[*map(int,input().split())] for _ in range(n)]
board2 = [list(i) for i in zip(*board)]

bridge=[]
# 가로 가능한 다리
for i in range(n):
    for j in range(m-2):
        if board[i][j]==1 and board[i][j+1]==0 and board[i][j+2]==0:
            brid=[]
            k=j
            while board[i][k+1]==0 and k<m-2:
                k+=1
                brid.append((i,k))
            if k<m-1 and board[i][k+1]==1:
                bridge.append((brid,len(brid)))

# 세로 가능한 다리
for i in range(m):
    for j in range(n-2):
        if board2[i][j]==1 and board2[i][j+1]==0 and board2[i][j+2]==0:
            brid=[]
            k=j
            while board2[i][k+1]==0 and k<n-2:
                k+=1
                brid.append((k,i))
            if k<n and board2[i][k+1]==1:
                bridge.append((brid,len(brid)))

# 가능한 다리 모든 조합
ans=9**9
for i in range(1,len(bridge)+1):
    for j in c(bridge,i):
        board3=[k[:] for k in board]
        result=check(j)
        if result>ans:
            continue
        else:
            visit=[[0]*m for _ in range(n)]
            cnt=0
            for a in range(n):
                for b in range(m):
                    if board3[a][b]==1 and visit[a][b]<1:
                        isone(a,b)
            # print(cnt,result, ans, i, j, visit, board3)
            if cnt==1:
                ans=min(ans,result)
if ans==9**9:
    print(-1)
else:
    print(ans)