import sys
sys.stdin=open('input.txt','r')
from itertools import permutations as p

def bt(res,num=0):
    global ans
    if num==n:
        ans=max(ans,res*100)
    if res*100<ans:
        return
    for i in range(n):
        if V[i]<1 and P[num][i]:
            res=res*P[num][i]
            V[i]=1
            bt(res,num+1)
            V[i]=0
            res=res/P[num][i]

for t in range(1,1+int(input())):
    n=int(input())
    P=[[*map(lambda x:x/100,map(int,input().split()))] for _ in 'a'*n]
    V=[0]*n
    ans=0
    bt(1)
    print('#%i %.6f'%(t,ans))