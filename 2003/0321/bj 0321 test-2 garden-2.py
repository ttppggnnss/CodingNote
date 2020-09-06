# 시간초과
import sys
sys.stdin=open('../input.txt','r')
import time
start=time.time()
from itertools import combinations as c

n,m,g,r=map(int,input().split())
garden=[]
gland=set()
for i in range(n):
    garden.append([*map(int,input().split())])
    for j in range(m):
        if garden[i][j]==2:
            gland.add((i,j))
ans=0
di=[0,0,1,-1]
dj=[1,-1,0,0]
for i2 in c(gland,g):
    for j2 in c(gland-{*i2},r):
        flower=set()
        green=set(i2)
        red=set(j2)
        visit=green|red
        while green and red:
            new_green=set()
            new_red=set()
            for p in green:
                i,j=p
                for k in range(4):
                    ni,nj=i+di[k],j+dj[k]
                    if -1<ni<n and -1<nj<m and (ni,nj) not in visit:
                        if garden[ni][nj]==1 or garden[ni][nj]==2:
                            new_green.add((ni,nj))
            for q in red:
                i,j=q
                for k in range(4):
                    ni,nj=i+di[k],j+dj[k]
                    if -1<ni<n and -1<nj<m and (ni,nj) not in visit:
                        if garden[ni][nj]==1 or garden[ni][nj]==2:
                            new_red.add((ni,nj))
            flower=flower|(new_green&new_red)
            visit=visit|new_green|new_red
            red=new_red-flower
            green=new_green-flower
        ans=max(ans,len(flower))
print(ans)
print(time.time()-start)