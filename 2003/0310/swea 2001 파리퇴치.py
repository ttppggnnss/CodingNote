import sys
sys.stdin=open('input.txt','r')

for t in range(1, int(input())+1):
    n,m=map(int,input().split())
    b=[[*map(int,input().split())]for _ in'a'*n]
    ans=0
    for i in range(n-m+1):
        for j in range(n-m+1):
            res=0
            for k in range(m):
                res+=sum(b[i+k][j:j+m])
            ans=max(ans,res)
    print('#%i'%t,ans)