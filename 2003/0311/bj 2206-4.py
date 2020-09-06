import sys
sys.stdin=open('input.txt', 'r')
import time
start=time.time()
di,dj=[1,-1,0,0],[0,0,1,-1]
n,m=map(int,input().split())
b=[[*map(int,input())] for _ in'a'*n]
ans=9**9
q=[((0,0),0,{(0,0)},1)]
while q:
    i,dig,v,cnt=q.pop()
    if cnt>=ans:
        continue
    if i==(n-1,m-1):
        ans=min(cnt,ans)
        continue
    for k in range(4):
        ni,nj=i[0]+di[k],i[1]+dj[k]
        if -1<ni<n and -1<nj<m and (ni,nj) not in v and b[ni][nj]<1:
            q.append(((ni,nj),dig,v|{(ni,nj)},cnt+1))
        elif -1<ni<n and -1<nj<m and (ni,nj) not in v and b[ni][nj] and dig<1:
            q.append(((ni,nj),1,v|{(ni,nj)},cnt+1))
if ans<9**9:print(ans)
else:print(-1)
print(time.time()-start)