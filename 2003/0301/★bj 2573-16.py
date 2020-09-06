# 문제를 잘못 이해함 but 시간 초과
import sys
sys.stdin=open('input.txt','r')
input=sys.stdin.readline
D=(1,0),(-1,0),(0,1),(0,-1)
def cnt0(i,j):
    cnt=0
    for di,dj in D:
        ni,nj=i+di,j+dj
        if L[ni][nj]<1 and (ni,nj) not in r:
            cnt+=1
    return cnt

n,m=map(int,input().split())
L=[[*map(int,input().split())]for _ in'a'*n]
time=0
while 1:
    time+=1
    q=[]
    r=[]
    for i in range(n):
        for j in range(m):
            if L[i][j]>0:
                L[i][j]-=cnt0(i,j)
                if L[i][j]>0:q.append((i,j))
                else:r.append((i,j))
    if q:
        p=[q.pop()]
        while p:
            y,x=p.pop()
            for dy,dx in D:
                ny,nx=y+dy,x+dx
                if (ny,nx) in q:
                    q.remove((ny,nx))
                    p.append((ny,nx))
    else:
        print(0)
        break
    if q:
        print(time)
        break