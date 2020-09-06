import sys
sys.stdin=open('input.txt','r')

n,m=map(int,input().split())
c=[]
b=[];z=0
for i in range(n):
    b.append([*map(int,input().split())])
    for j in range(m):
        for k in range(1,6):
            if b[i][j]==k:
                c.append((i,j,k))
                z+=1
ans=0
for i in b:
    ans+=i.count(0)
di=[-1,0,1,0]
dj=[0,1,0,-1]
bs=[]
if c:
    i,j,k=c[0]
    que=[(i,j,k,[d[:] for d in b],1)]
    while que:
        i,j,k,b2,cnt=que.pop()
        b2[i][j]=-k
        if cnt<z:
            p,q,r=c[cnt]
        if k==1:
            for e in range(4):
                b3 = [d[:] for d in b2]
                ni, nj = i + di[e], j + dj[e]
                if -1 < ni < n and -1 < nj < m:
                    while -1 < ni < n and -1 < nj < m and b3[ni][nj] != 6:
                        b3[ni][nj] = '#'
                        ni, nj = ni + di[e], nj + dj[e]
                if cnt == z:
                    bs.append(b3)
                else:
                    que.append((p, q, r, b3, cnt + 1))
        if k==2:
            for f in (0,2),(1,3):
                b3 = [d[:] for d in b2]
                for e in f:
                    ni, nj = i + di[e], j + dj[e]
                    if -1 < ni < n and -1 < nj < m:
                        while -1 < ni < n and -1 < nj < m and b3[ni][nj] != 6:
                            b3[ni][nj] = '#'
                            ni, nj = ni + di[e], nj + dj[e]
                if cnt == z:
                    bs.append(b3)
                else:
                    que.append((p, q, r, b3, cnt + 1))
        if k==3:
            for f in (0,1),(1,2),(2,3),(3,0):
                b3=[d[:]for d in b2]
                for e in f:
                    ni, nj = i + di[e], j + dj[e]
                    if -1 < ni < n and -1 < nj < m:
                        while -1 < ni < n and -1 < nj < m and b3[ni][nj] != 6:
                            b3[ni][nj] = '#'
                            ni, nj = ni + di[e], nj + dj[e]
                if cnt == z:
                    bs.append(b3)
                else:
                    que.append((p, q, r, b3, cnt + 1))
        if k==4:
            for f in (0,1,2),(1,2,3),(2,3,0),(3,0,1):
                b3 = [d[:] for d in b2]
                for e in f:
                    ni, nj = i + di[e], j + dj[e]
                    if -1 < ni < n and -1 < nj < m:
                        while -1 < ni < n and -1 < nj < m and b3[ni][nj] != 6:
                            b3[ni][nj] = '#'
                            ni, nj = ni + di[e], nj + dj[e]
                if cnt == z:
                    bs.append(b3)
                else:
                    que.append((p, q, r, b3, cnt + 1))
        if k==5:
            b3=[d[:] for d in b2]
            for e in range(4):
                ni, nj = i + di[e], j + dj[e]
                if -1<ni<n and -1<nj<m:
                    while -1<ni<n and -1<nj<m and b3[ni][nj] != 6:
                        b3[ni][nj] = '#'
                        ni, nj = ni + di[e], nj + dj[e]
            if cnt == z:
                bs.append(b3)
            else:
                que.append((p, q, r, b3, cnt + 1))
    for b3 in bs:
        res=0
        for i in b3:
            res+=i.count(0)
        ans=min(res,ans)
print(ans)



