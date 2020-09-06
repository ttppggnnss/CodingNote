import sys
sys.stdin=open('../input.txt','r')

def bt(i,n,cb):
    global a
    if i==n:a+=1;return
    for j in range(n):
        if cb[i][j]<1:
            cb2=[k[:] for k in cb]
            for di,dj in(1,-1),(1,0),(1,1):
                ni,nj=i+di,j+dj
                while ni<n and -1<nj<n:
                    cb2[ni][nj]=1
                    ni,nj=ni+di,nj+dj
            bt(i+1,n,cb2)
for t in range(1,int(input())+1):
    n=int(input());a=0
    bt(0,n,[[0]*n for _ in'a'*n])
    print('#%i'%t,a)
