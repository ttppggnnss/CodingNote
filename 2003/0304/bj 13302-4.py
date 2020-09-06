import sys
sys.stdin=open('input.txt', 'r')
input=sys.stdin.readline

def f(i,j,v):
    if dp[i][j]>v:
        dp[i][j]=v

d1,d3,d5=10000,25000,37000
n,m=map(int,input().split())
v=[1]+[0]*n+[1] # 총 n+2개
if m:
    L=[*map(int,input().split())]
    # 못가는 날
    for i in L:
        v[i]=1
# 최대값으로 초기화
# dp[n+1] 에서 최소 값을 찾을 것
# n: 쿠폰개수 n+2: 전체 날짜
dp=[[9**9]*n for _ in 'a'*(n+2)]
dp[0][0]=0
for i in range(n+1):# 날짜 (v[n]까지 가야하므로)
    for j in range(max(3*n//5,1)):# 쿠폰 수 넉넉하게 하지만 적어도 1이상 되도록
        # 못가는 날
        if v[i]:
            f(i+1,j,dp[i][j])

        # 쿠폰 3개 이상 이면 하루 넘어간다
        if j>=3:
            f(i+1,j-3,dp[i][j])

        # 1일권
        f(i+1,j,dp[i][j]+d1)

        # 3일권
        if i<=n-2:
            for k in range(3):
                f(i+1+k,j+1,dp[i][j]+d3)

        # 5일권
        if i<=n-4:
            for k in range(5):
               f(i+1+k,j+2,dp[i][j]+d5)
for i in dp:
    print(*i)
ans=min(dp[n+1])
print(ans)
