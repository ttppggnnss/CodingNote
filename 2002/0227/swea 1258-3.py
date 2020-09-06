import sys
sys.stdin=open('input.txt','r')

def f(j,i,L):
    L.append((j,i))
    visited[j][i]=1
    for dj,di in (1,0),(0,1):
        nj,ni=j+dj,i+di
        if nj<n and ni<n:
            if M[nj][ni]>0 and visited[nj][ni]<1:
                L=f(nj,ni,L)
    return L


for t in range(1,int(input())+1):
    n=int(input())
    M=[[*map(int,input().split())]for _ in[0]*n]
    visited=[[0]*n for _ in [0]*n]
    ans=[]
    for i in range(n):
        for j in range(n):
            if M[j][i]>0 and visited[j][i]<1:
                L=f(j,i,[])
                y=max(L)[0]-min(L)[0]+1
                x=max(L)[1]-min(L)[1]+1
                ans.append((y,x))
    ans=sorted(ans, key=lambda x:(x[0]*x[1],x[0]))
    print("#%i"%t,len(ans), end=" ")
    for i in ans:
        print(*i, end=" ")
    print()