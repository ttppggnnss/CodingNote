import sys
sys.stdin=open('input.txt', 'r')
import time
start=time.time()
from collections import deque
dx,dy=[1,-1,0,0],[0,0,1,-1]
n,m=map(int,input().split())
b=[[*map(int,input().rstrip())] for _ in'a'*n]
d=[[[-1]*2 for _ in'a'*m]for __ in'b'*n];d[0][0][0]=1
q=deque([(0,0,0)])
while q:
    x,y,z,=q.popleft()
    for k in range(4):
        nx,ny=x+dx[k],y+dy[k]
        if -1<nx<n and -1<ny<m and b[nx][ny]<1 and d[nx][ny][z]<0:
            d[nx][ny][z]=d[x][y][z]+1
            q.append((nx,ny,z))
        if z<1 and -1<nx<n and -1<ny<m and b[nx][ny] and d[nx][ny][1]<0:
            d[nx][ny][z+1]=d[x][y][z]+1
            q.append((nx,ny,z+1))
if -1 in d[n-1][m-1]:
    print(max(d[n-1][m-1]))
else:
    print(min(d[n-1][m-1]))
print(time.time()-start)