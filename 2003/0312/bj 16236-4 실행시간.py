# 실행시간
import sys
sys.stdin=open('input.txt','r')

dy=[-1,0,0,1]
dx=[0,-1,1,0]
def IS(y,x,s):
    if -1<y<N and -1<x<N and A[y][x]<=s:return True
    return False
def BFS(y,x,s,c,r):
    global R
    while True:
        M=[[0]*N for _ in range(N)]
        if c==0:s+=1;c=s
        Q=[]
        Q.append([y,x,r])
        M[y][x]=9
        t=1
        d=999
        dq=[]
        while Q:
            tmp=Q.pop(0)
            hY=tmp[0]
            hX=tmp[1]
            hr=tmp[2]
            if hr>d:break
            if 0<A[hY][hX]<s:
                if hr<d:d=hr
                t=0
                dq.append([hY,hX,hr])
            for dir in range(4):
                nY=hY+dy[dir]
                nX=hX+dx[dir]
                if IS(nY,nX,s) and not M[nY][nX]:Q.append([nY,nX,hr+1]);M[nY][nX]=9
        if t:break
        else:
            dq.sort()
            y=dq[0][0]
            x=dq[0][1]
            A[y][x] = 0
            c-=1
            R+=d
N=int(input())
A=[[int(x)for x in input().split()]for y in range(N)]
R=0
for i in range(N):
    for j in range(N):
        if A[i][j]==9:
            A[i][j]=0
            BFS(i,j,2,2,0)
print(R)