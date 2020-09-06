# 시간 초과
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
        garden2=[k[:] for k in garden]
        for i3 in i2:
            garden2[i3[0]][i3[1]]='G'
        for j3 in j2:
            garden2[j3[0]][j3[1]]='R'
        ans2=0
        while 1:
            check=[k[:] for k in garden2]
            for i4 in range(n):
                for j4 in range(m):
                    if check[i4][j4]=='G':
                        garden2[i4][j4]='g'
                        for k2 in range(4):
                            ni,nj=i4+di[k2],j4+dj[k2]
                            if -1<ni<n and -1<nj<m:
                                if garden2[ni][nj]==1 or garden2[ni][nj]==2:
                                    garden2[ni][nj]='G'
                                if garden2[ni][nj]=='R' and check[ni][nj]!='R':
                                    garden2[ni][nj]='F'
                                    ans2+=1
                    if check[i4][j4] =='R':
                        garden2[i4][j4]='r'
                        for k2 in range(4):
                            ni,nj=i4+di[k2],j4+dj[k2]
                            if -1 < ni < n and -1 < nj < m:
                                if garden2[ni][nj]==1 or garden2[ni][nj]==2:
                                    garden2[ni][nj]='R'
                                if garden2[ni][nj]=='G' and check[ni][nj]!='G':
                                    garden2[ni][nj]='F'
                                    ans2+=1
            if check==garden2:break
        ans=max(ans2,ans)
print(ans)
print(time.time()-start)