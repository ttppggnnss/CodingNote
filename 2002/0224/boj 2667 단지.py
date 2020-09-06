# https://www.acmicpc.net/problem/2667

import sys
sys.stdin=open('input.txt','r')

n=int(input())
L=[[*map(int,input())] for _ in [0]*n]
ans=[]
for i in range(n):
    for j in range(n):
        if L[i][j]==1:
            L[i][j]=0
            cnt=1
            q=[(j,i)]
            while q:
                x0,y0=q.pop()
                for dx,dy in (0,1),(0,-1),(1,0),(-1,0):
                    nx,ny = x0+dx,y0+dy
                    if 0<=ny<n and 0<=nx<n:
                        if L[ny][nx]==1:
                            L[ny][nx]=0
                            q.append((nx,ny))
                            cnt+=1
            ans.append(cnt)
print(len(ans),*sorted(ans),sep='\n')