import sys
sys.stdin=open('input.txt','r')

for t in range(1,int(input())+1):
    n,m=map(int,input().split())
    A=[*map(int,input().split())]
    B=[*map(int,input().split())]
    ans=0
    if n>m:
        for i in range(n-m+1):
            res=0
            c=i
            for j in range(m):
                res+=A[c]*B[j]
                c+=1
            ans=max(ans,res)
    else:
        for i in range(m-n+1):
            res=0
            c=i
            for j in range(n):
                res+=A[j]*B[c]
                c+=1
            ans=max(ans,res)
    print('#%i'%t,ans)
