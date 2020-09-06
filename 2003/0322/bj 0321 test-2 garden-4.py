# ??
# set 으로 관리하면 시간
# sys.stdin.readline 이용

import sys
sys.stdin=open('../input.txt','r')
import time
start=time.time()

import sys

def check(a):
    for a_ in a:
        visit[a_[0]][a_[1]]=0
    return

from itertools import combinations as c

n,m,g,r=map(int,sys.stdin.readline().split())
garden=[]
gland=set()
for i in range(n):
    garden.append([*map(int,sys.stdin.readline().split())])
    for j in range(m):
        if garden[i][j]==2:
            gland.add((i,j))
ans=0
di=[0,0,1,-1]
dj=[1,-1,0,0]
for i2 in c(gland,g):
    for j2 in c(gland-{*i2},r):
        visit=[z[:]for z in garden]
        flower=set()
        green=set(i2)
        red=set(j2)
        check(green)
        check(red)
        while green and red:
            new_green=set()
            new_red=set()
            for p in green:
                i,j=p
                for k in range(4):
                    ni,nj=i+di[k],j+dj[k]
                    if -1<ni<n and -1<nj<m and (ni,nj) and visit[ni][nj]:
                        new_green.add((ni,nj))
            for q in red:
                i,j=q
                for k in range(4):
                    ni,nj=i+di[k],j+dj[k]
                    if -1<ni<n and -1<nj<m and (ni,nj) and visit[ni][nj]:
                        new_red.add((ni,nj))
            check(new_green)
            check(new_red)
            flower=flower|(new_green&new_red)
            red=new_red-flower
            green=new_green-flower
        ans=max(ans,len(flower))
print(ans)
print(time.time()-start)


