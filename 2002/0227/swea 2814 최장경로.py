import sys
sys.stdin=open('input.txt','r')

def bt(ans,cnt,j):
    if ans<cnt:ans=cnt
    for x,i in enumerate(L[j]):
        if i and V[x]<1:
            V[x]=1;cnt+=1
            ans=bt(ans,cnt,x)
            V[x]=0;cnt-=1
    return ans
for t in range(1,int(input())+1):
    n,m=map(int,input().split());L=[[0]*n for _ in [0]*n]
    for i in range(m):
        a,b=map(int,input().split())
        L[a-1][b-1]+=1;L[b-1][a-1]+=1
    V=[0]*n;ans=1;cnt=0
    for i in range(n):
        for x,j in enumerate(L[i]):
            if j:
                V[x]=1;cnt+=1
                ans=bt(ans,cnt,x)
                cnt-=1;V[x]=0
    print('#%i'%t, ans)

