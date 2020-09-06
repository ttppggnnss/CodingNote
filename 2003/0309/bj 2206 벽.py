# 시간 초과

import sys
sys.stdin=open('input.txt', 'r')
from collections import deque

def dig():
    bs=[b]
    for i in range(n):
        for j in range(m):
            b2 = [[a for a in c] for c in b]
            if b2[i][j]==1:
                b2[i][j]-=1
                bs.append(b2)
    return bs
di,dj=[1,-1,0,0],[0,0,1,-1]

def trail(s,b,v):
    global g,res
    q=deque([s])
    cnt=1
    while q:
        cnt+=1
        for _ in range(len(q)):
            i,j=q.popleft()
            for k in range(4):
                ni,nj=i+di[k],j+dj[k]
                if -1<ni<n and -1<nj<m and (ni,nj) not in v and b[ni][nj]<1:
                    v.add((ni,nj))
                    q.append((ni,nj))
        if g in q:
            return cnt
    return 9**9

n,m=map(int,input().split())
b=[[*map(int,input())] for _ in'a'*n]
s=(0,0)
g=(n-1,m-1)
ans=[]
for b2 in dig():
    res=trail(s,b2,{s})
    ans.append(res)
if min(ans)<9**9:
    print(min(ans))
else:
    print(-1)