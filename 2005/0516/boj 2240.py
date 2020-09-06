import sys
sys.stdin=open('../input.txt', 'r')

T, W = map(int, input().split())
dp=[[[0,0] for _ in range(W+2)] for _ in range(T+1)]
for i in range(1,T+1):
    b = int(input())
    if b==1:
        for j in range(1,W+2):
            dp[i][j][0]=max(dp[i-1][j][0]+1,dp[i-1][j-1][1]+1)
    else:
        for j in range(1,W+2):
            dp[i][j][1]=max(dp[i-1][j][1]+1, dp[i-1][j-1][0]+1)
print(max(dp[-1][-1]))