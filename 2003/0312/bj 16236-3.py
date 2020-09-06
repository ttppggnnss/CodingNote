# 파이썬 시간 초과
# pypy 통과 시간 늘어남 ??
import sys
sys.stdin=open('input.txt','r')
from collections import deque
di=[1,-1,0,0]
dj=[0,0,1,-1]
def f(s,g,size):
    v=[[0]*n for _ in'a'*n]
    cnt=0
    q=deque([s])
    v[s[0]][s[1]]=1
    while q:
        cnt+=1
        for i in range(len(q)):
            i,j=q.popleft()
            for r in range(4):
                ni,nj=i+di[r],j+dj[r]
                if -1<ni<n and -1<nj<n and b[ni][nj]<=size and v[ni][nj]<1:
                    v[ni][nj]=1
                    q.append((ni,nj))
        if v[g[0]][g[1]]>0:return cnt
    return 9**9

n=int(input())
b=[];fish=[]
for i in range(n):
    b.append([*map(int,input().split())])
    for j in range(n):
        if 0<b[i][j]<7:fish.append(((i,j),b[i][j]))
        if b[i][j]>8:baby_shark=(i,j);b[i][j]=0
ans=0;size=2;grow=0
while fish:
    check=fish[:]
    if grow<1:fish2=[i for i in fish if i[1]<size]
    if fish2:
        res=9**9;z=(n-1,n-1),size-1
        for i in fish2:
            a=f(baby_shark,i[0],size)
            if a<res:
                res=a
                z=i
            if a==res:
                if z[0][0]>i[0][0]:z=i
                if z[0][0]==i[0][0]:
                    if z[0][1]>i[0][1]:z=i
        if res<9**9:
            fish.remove(z)
            fish2.remove(z)
            ans+=res
            grow+=1
            if grow==size:
                size+=1
                grow=0
            baby_shark=(z[0])
        else:break
    if check==fish:break
print(ans)