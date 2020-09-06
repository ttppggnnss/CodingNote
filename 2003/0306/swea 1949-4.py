import sys
sys.stdin=open('input.txt', 'r')

def f(y,x,k):
    visited=[0]*n*n
    visited[y*n+x]=1
    s=[(y,x,1,0,board[y][x],visited[:])]
    res=1
    while s:
        y_,x_,cnt,dig,now,visited=s.pop()
        res=max(res,cnt)
        for dy,dx in (1,0),(-1,0),(0,1),(0,-1):
            ny,nx=y_+dy,x_+dx
            if -1<ny<n and -1<nx<n and board[ny][nx]<now and visited[ny*n+nx]<1:
                visited[ny*n+nx]=1
                s.append((ny,nx,cnt+1,dig,board[ny][nx],visited[:]))
                visited[ny*n+nx]=0
            elif not dig and -1<ny<n and -1<nx<n and board[ny][nx]-k<now and visited[ny*n+nx]<1:
                for c in range(1,k+1):
                    if board[ny][nx]-c<now:
                        visited[ny*n+nx]=1
                        s.append((ny,nx,cnt+1,dig+1,board[ny][nx]-c,visited[:]))
                        visited[ny*n+nx]=0
    return res
for t in range(1,int(input())+1):
    n,k=map(int,input().split())
    board=[[*map(int,input().split())]for _ in'a'*n]
    mxh=0
    for i in range(n*n):
        mxh=max(board[i//n][i%n],mxh)
    ans=1
    for i in range(n*n):
        if board[i//n][i%n]==mxh:
            res=f(i//n,i%n,k)
            ans=max(ans,res)
    print('#%i'%t,ans)