# 답 다르게 나옴 이상함

import sys
sys.stdin=open('input.txt','r')
input=sys.stdin.readline

def solve(day,coupon,price):
    if n<day:
        return price
    if dp[day][coupon]:
        return dp[day][coupon]+price
    if v[day]:
        return solve(day+1,coupon,price)

    ans=1<<31-1
    ans=min(ans,solve(day+1,coupon,price+10000))
    ans=min(ans,solve(day+3,coupon+1,price+25000))
    ans=min(ans,solve(day+5,coupon+2,price+37000))

    if coupon>=3:
        ans=min(ans,solve(day+1,coupon-3,price))

    dp[day][coupon]=ans-price
    return ans

n,m=map(int,input().split())
v=[0]*110
L=[*map(int,input().split())]
dp=[[0]*110 for _ in'a'*110]
for i in L:
    v[i-1]=1

print(solve(1,0,0))

#
# int solve(int day, int coupon, int price){
# 	if(n < day) return price; //범위 초과 시 현재 가격 반환
# 	if(dp[day][coupon]) return dp[day][coupon] + price; //이미 탐색했을 경우
# 	if(v[day]) return solve(day+1, coupon, price); //불가능한 날짜면 다음날을 탐색
#
# 	int ans = (1<<31)-1;
# 	ans = min(ans, solve(day+1, coupon, price+10000)); //1일권 구매
# 	ans = min(ans, solve(day+3, coupon+1, price+25000)); //3일권 구매 + 쿠폰 1개
# 	ans = min(ans, solve(day+5, coupon+2, price+37000)); //5일권 구매 + 쿠폰 2개
#
# 	if(coupon >= 3){ //쿠폰 사용 가능 시
# 		ans = min(ans, solve(day+1, coupon-3, price));
# 	}
#
# 	dp[day][coupon] = ans - price;
# 	return ans;
# }
#
# int main(){
# 	ios_base::sync_with_stdio(0); cin.tie(0);
# 	cin >> n >> m;
# 	for(int i=0; i<m; i++){
# 		int t; cin >> t; v[t] = 1;
# 	}
# 	cout << solve(1, 0, 0);
# }