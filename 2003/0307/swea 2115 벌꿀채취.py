# 풀긴 했는데 비효율적
import sys
sys.stdin=open('input.txt', 'r')
from itertools import permutations as p

def f(b,c):
    a=0
    for k in p(b):
        d=c
        r=0
        for i in range(m):
            if k[i]<=d:
                d-=k[i]
                r+=k[i]**2
            else:
                break
        a=max(a,r)
    return a

def f2(b,c):
    d=0
    for i in range(n-2*m+1):
        d=0
        x=f(b[i:i+m],c)
        for j in range(i+m,n-m+1):
            y=f(b[j:j+m],c)
        d=max(c,x+y)
    return d

for t in range(1,int(input())+1):
    n,m,c=map(int,input().split())
    L=[[*map(int,input().split())]for _ in'a'*n]
    ans=[]
    ans3=[]
    for i in L:
        ans2=[]
        ans3.append(f2(i,c))
        for j in range(n-m+1):
            ans2.append(f(i[j:j+m],c))
        ans.append(max(ans2))
    ans=sorted(ans)
    print('#%i'%t,max(sum(ans[-2:]),max(ans3)))
