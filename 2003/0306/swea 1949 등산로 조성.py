import sys
sys.stdin=open('input.txt', 'r')

def dig(k):
    bs=[]
    for i in range(n):
        for j in range(n):
            for r in range(1,k+1):
                b2 = [[a for a in c] for c in b]
                b2[i][j]-=r
                bs.append(b2)
    return bs
di,dj=[1,-1,0,0],[0,0,1,-1]
def trail(i,b,v):
    for k in range(4):
        ni,nj=i[0]+di[k],i[1]+dj[k]
        if -1<ni<n and -1<nj<n and (ni,nj) not in v and b[ni][nj]<b[i[0]][i[1]]:
            v.add((ni,nj))
            trail((ni,nj),b,v)
            v-={(ni,nj)}
    else:
        global res
        res=max(res,len(v))

for t in range(1,int(input())+1):
    n,k=map(int,input().split())
    b=[];mx=0
    for i in range(n):
        b.append([*map(int,input().split())])
        mx=max(max(b[-1]),mx)
    s=[]
    for i in range(n):
        for j in range(n):
            if b[i][j]==mx:
                s.append((i,j))
    ans=0
    for i in s:
        for b2 in dig(k):
            res=0
            if b2[i[0]][i[1]]==mx:
                trail(i,b2,{i})
                ans=max(ans,res)
    print('#%i'%t,ans)