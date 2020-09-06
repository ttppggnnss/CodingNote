import sys
sys.stdin=open('../input.txt', 'r')
n, s, m = map(int, input().split())
V =[0]+[*map(int, input().split())]
dp = [[0]*(m+1) for _ in range(n+1)]
dp[0][s]=1
for i in range(1,n+1):
    for j in range(m+1):
        if dp[i-1][j]>0:
            if j-V[i]>=0:
                dp[i][j-V[i]]=1
            if j+V[i]<=m:
                dp[i][j+V[i]]=1
try:
    print(m-dp[n][::-1].index(1))
except:
    print(-1)