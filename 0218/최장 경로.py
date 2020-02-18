import sys
sys.stdin=open('최장경로.txt','r')

def linked(i,V):
    global ans
    for k,j in enumerate(V):
        if L[i][j]>0:
            L[i][j]-=1
            L[j][i]-=1
            V.remove(j)
            linked(j,V)
            V.insert(k,j)
            L[j][i]+=1
            L[i][j]+=1
    if ans<n-len(V):
        ans=n-len(V)

for t in range(1,int(input())+1):
    n,m = map(int,input().split())
    L=[[0]*n for _ in [0]*n]
    for _ in [0]*m:
        x,y=map(int,input().split())
        L[x-1][y-1]+=1
        L[y-1][x-1]+=1
    V=list(range(n))
    ans=1
    for i in range(n):
        linked(i,V)

    print('#%d'%t,ans)