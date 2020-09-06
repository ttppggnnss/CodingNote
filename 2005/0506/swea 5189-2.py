import sys
sys.stdin=open('../input.txt', 'r')

def f(i,j,cnt,res=0):
    res+=board[i][j]
    if cnt==n-2:
        global ans
        ans=min(ans,res+board[j][0])
        return
    for k in range(1,n):
        if board[j][k]>0 and visit[k]<1:
            visit[k]=1
            f(j,k,cnt+1,res)
            visit[k]=0

for t in range(1, int(input())+1):
    n=int(input())
    board=[[*map(int,input().split())] for _ in range(n)]
    ans=9**9
    visit=[0]*n
    for i in range(1,n):
        visit[i]=1
        f(0,i,0,0)
        visit[i]=0
    print('#%i'%t, ans)