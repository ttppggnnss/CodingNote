import sys
sys.stdin=open('input.txt', 'r')
input=sys.stdin.readline

def f(i,j,v):
    if dp[i][j]>v:dp[i][j]=v

d1,d3,d5=10000,25000,37000
n,m=map(int,input().split())
v=[1]+[0]*n+[1]
L=[*map(int,input().split())]
# 못가는 날
for i in L:
    v[i]=1
# 최대값으로 초기화
# dp[n] 에서 최소 값을 찾을 것
dp=[[9**9]*n for _ in 'a'*(n+2)]
dp[0][0]=0
for i in range(n+1):# 날짜
    for j in range(3*n//5):# 쿠폰 수
        # 못가는 날
        if v[i]:
            f(i+1,j,dp[i][j])
        # 쿠폰 3개 이상 이면 하루 넘어간다
        if j>=3:
            f(i+1,j-3,dp[i][j])

        # 1일권
        f(i+1,j,dp[i][j]+d1)
        # 3일권
        if i<=n-3:
            for k in range(1,4):
                f(i+k,j+1,dp[i][j]+d3)
        # 5일권
        if i<=n-5:
            for k in range(1,6):
               f(i+k,j+2,dp[i][j]+d5)
# for i in dp:
#     print(*i)
ans=9**9
for j in range(n):
    ans=min(ans,dp[n+1][j])
print(ans)


# #include <bits/stdc++.h>
# using namespace std;
#
# const int n_ = 100 + 10;
# const int price[] = { 0,10000,25000,37000 };
#
# const int INF = 987654321;
#
# int n, m;
# int dp[n_][n_ * 2];
# bool chk[n_];
#
# void upd(int i, int j, int v) {
# 	if (dp[i][j] > v || dp[i][j] == INF) dp[i][j] = v;
# }
#
# int main() {
# 	scanf("%d %d", &n, &m);
# 	for (int i = 0; i < m; i++) {
# 		int a;
# 		scanf("%d", &a);
# 		chk[a] = true;
# 	}
#
# 	for (int i = 0; i <= n; i++)
# 		for (int j = 0; j <= n * 2; j++)
# 			dp[i][j] = INF;
#
# 	dp[0][0] = 0;
# 	for (int i = 0; i < n; i++) {
# 		for (int j = 0; j <= i * 2; j++) {
# 			if (dp[i][j] == INF) continue;
# 			if (chk[i + 1]) upd(i + 1, j, dp[i][j]);
# 			if (j >= 3) upd(i + 1, j - 3, dp[i][j]);
#
# 			upd(i + 1, j, dp[i][j] + price[1]);
# 			for (int k = 1; k <= 3; k++)
# 				upd(i + k, j + 1, dp[i][j] + price[2]);
# 			for (int k = 1; k <= 5; k++)
# 				upd(i + k, j + 2, dp[i][j] + price[3]);
# 		}
# 	}
#
# 	int ans = INF;
# 	for (int j = 0; j < n * 2; j++)
# 		ans = min(ans, dp[n][j]);
#
# 	printf("%d", ans);
#
# 	return 0;
# }