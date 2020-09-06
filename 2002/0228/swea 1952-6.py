import sys
sys.stdin=open('input.txt','r')

for t in range(1,int(input())+1):
    a, b, c, d=map(int,input().split())
    plan=[*map(int,input().split())]
    memo=[0]*13
    for m,p in enumerate(plan,1):
        if p:
            memo[m]=min(memo[m-1]+a*p,memo[m-1]+b,memo[m-1]+c)
        else:
            memo[m]=memo[m-1]
        if m>2:
            memo[m]=min(memo[m],memo[m-3]+c)
    print('#%i'%t,min(d,memo[-1]))
