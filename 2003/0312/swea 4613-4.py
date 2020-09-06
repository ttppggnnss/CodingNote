import sys
sys.stdin=open('input.txt','r')

for t in range(1,int(input())+1):
    n,m=map(int,input().split());flag=[[*input()] for _ in'a'*n];ans=9**9;w=b=r=0
    for i in range(0,n-2):
        w+=m-flag[i].count('W');b=w
        for j in range(i+1,n-1):
            b+=m-flag[j].count('B');r=b
            for k in range(j+1,n):
                r+=m-flag[k].count('R')
            ans=min(ans,r)
    print('#%i'%t,ans)