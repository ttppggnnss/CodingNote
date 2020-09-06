import sys
sys.stdin=open('input.txt','r')
dy=[-1,0,1,0]
dx=[0,1,0,-1]
ps=[[],[0,1,2,3],[0,2],[1,3],[0,1],[1,2],[2,3],[3,0]]
pl=[[1,2,5,6],[1,3,6,7],[1,2,4,7],[1,3,4,5]]
for t in range(int(input())):
    n,m,r,c,l=map(int,input().split())
    L=[[*map(int,input().split())] for _ in 'a'*n]
    S=[(r,c)]
    V={(r,c)}
    ans=1
    while S:
        if l==1:
            break
        l-=1
        for i in 'a'*len(S):
            d,e=S.pop(0)
            for i in ps[L[d][e]]:
                if 0<=d+dy[i]<n and 0<=e+dx[i]<m and L[d+dy[i]][e+dx[i]] in pl[i] and (d+dy[i],e+dx[i]) not in V:
                    S.append((d+dy[i],e+dx[i]))
                    V.add((d+dy[i],e+dx[i]))
                    ans+=1
    print('#%i'%(t+1),ans)

