import sys
sys.stdin=open('input.txt','r')

def dfs(s,cnt=1):
    cnt+=1
    for i in V[s]:
        if p[i]==0 or p[i]>cnt:
            p[i]=cnt
            dfs(i,cnt)

for t in range(1,11):
    v,s=map(int,input().split())
    c=[*map(int,input().split())]
    V=[[]for i in'a'*101]
    q=[[] for _ in 'a'*101]
    p=[0]*101
    p[s]=1
    for i in range(v//2):V[c[2*i]]+=[c[2*i+1]]
    dfs(s)
    start=0
    m=max(p)
    for i in range(p.count(m)):
        ans=p.index(m,start)
        start=ans+1
    print('#%d'%t,ans)