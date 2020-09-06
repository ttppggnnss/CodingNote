# 실행시간
import sys
sys.stdin=open('input.txt','r')

dy=[-1,0,0,1]
dx=[0,-1,1,0]
def BFS(y,x,s,c,r):
    global ans
    while True:
        v=[[0]*n for _ in range(n)]
        if c==0:s+=1;c=s
        Q=[]
        Q.append([y,x,r])
        v[y][x]=1
        t=1
        d=999
        dq=[]
        while Q:
            tmp=Q.pop(0)
            hY=tmp[0]
            hX=tmp[1]
            hr=tmp[2]
            if hr>d:break
            if 0<b[hY][hX]<s:
                if hr<d:d=hr
                t=0
                dq.append([hY,hX,hr])
            for dir in range(4):
                nY=hY+dy[dir]
                nX=hX+dx[dir]
                if -1<nY<n and -1<nX<n and b[nY][nX]<=s and v[nY][nX]<1:
                    Q.append([nY,nX,hr+1]);v[nY][nX]=1
        if t:break
        else:
            dq.sort()
            y=dq[0][0]
            x=dq[0][1]
            b[y][x] = 0
            c-=1
            ans+=d

n=int(input())
b=[[*map(int,input().split())]for _ in'a'*n]
ans=0
for i in range(n):
    for j in range(n):
        if b[i][j]==9:
            b[i][j]=0
            BFS(i,j,2,2,0)
print(ans)