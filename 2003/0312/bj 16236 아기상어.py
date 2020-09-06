# 시간초과
import sys
sys.stdin=open('input.txt','r')
from collections import deque
di=[1,-1,0,0]
dj=[0,0,1,-1]
def f(s,g,size):
    cnt=0
    q=deque([s])
    while q:
        if g in q:
            return cnt
        cnt+=1
        for i in range(len(q)):
            i,j=q.popleft()
            for r in range(4):
                ni,nj=i+di[r],j+dj[r]
                if -1<ni<n and -1<nj<n and b[ni][nj]<=size:
                    q.append((ni,nj))
    return 9**9

size=2
n=int(input())
b=[]
fish=[]
for i in range(n):
    b.append([*map(int,input().split())])
    for j in range(n):
        if 0<b[i][j]<7:
            fish.append((i,j,b[i][j]))
        if b[i][j]>8:
            baby_shark=(i,j)
ans=0;grow=0
while fish:
    check=fish[:]
    fish2=[i for i in fish if i[2]<size]
    if fish2:
        res=[];fish3=[]
        for i in fish2:
            res.append(f(baby_shark,(i[0],i[1]),size))
        if min(res)<9**9:
            for i in range(len(res)):
                if res[i]==min(res):
                    fish3.append(fish2[i])
            fish3=sorted(fish3, key=lambda x:(x[0],x[1]))
            # print(fish3, min(res),baby_shark,size)
            next_fish=fish3[0]
            i,j,k=fish3[0]
            fish.remove((i,j,k))
            ans+=f(baby_shark,(i,j),size)
            grow+=1
            if grow==size:
                size+=1
                grow=0
            b[baby_shark[0]][baby_shark[1]]=0
            baby_shark=(i,j)
            b[i][j]=9
        else:break
    if check==fish:
        break
print(ans)