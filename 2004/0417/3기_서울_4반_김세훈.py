# import sys
# sys.stdin=open('../input.txt','r')

def f(i,j):
    global ans
    visit[i][j]=1
    q=[(i,j)]
    while q:
        i,j=q.pop()
        for di in (-1,0,1):
            for dj in (-1,0,1):
                ni,nj=i+di,j+dj
                if -1<ni<10 and -1<nj<10 and board[ni][nj]>0 and visit[ni][nj]<1:
                    visit[ni][nj]=1
                    q.append((ni,nj))
    ans+=1
    return

for t in range(1, int(input())+1):
    board=[[*map(int,input().split())]for _ in range(10)]
    visit=[[0]*10 for _ in range(10)]
    ans=0
    for i in range(10):
        for j in range(10):
            if board[i][j]>0 and visit[i][j]<1:
                f(i,j)
    print('#%i'%t,ans)