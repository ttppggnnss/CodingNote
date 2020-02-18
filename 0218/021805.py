# 배열 최소 합

import sys
sys.stdin=open("input5.txt","r")

def minL(L,V,start,ans2):
    global ans
    if start==N:
        ans=min(ans,ans2)
    if ans2>ans:
        return
    for k,i in enumerate(V):
        ans2+=L[start][i]
        V.remove(i)
        minL(L,V,start+1,ans2)
        V.insert(k,i)
        ans2-=L[start][i]

for t in range(1,int(input())+1):
    N=int(input())
    L=[[*map(int,input().split())] for _ in[0]*N]
    V=list(range(N))
    ans=9*N
    minL(L,V,0,0)
    print("#%i"%t,ans)