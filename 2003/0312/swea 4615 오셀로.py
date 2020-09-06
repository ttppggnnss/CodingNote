import sys
sys.stdin=open('input.txt','r')

di=[-1,-1,0,1,1,1,0,-1]
dj=[0,1,1,1,0,-1,-1,-1]
def f(i,j,c):
    global b
    b[i][j]=c
    for k in range(8):
        ni,nj=i+di[k],j+dj[k]
        z=0
        while -1<ni<n and -1<nj<n and b[ni][nj]==3-c:
            ni,nj=ni+di[k],nj+dj[k]
            if -1<ni<n and -1<nj<n and b[ni][nj]==c:z=1
        if z:
            ni,nj=i+di[k],j+dj[k]
            while -1<ni<n and -1<nj<n and b[ni][nj]==3-c:
                b[ni][nj]=c
                ni,nj=ni+di[k],nj+dj[k]

for t in range(1,int(input())+1):
    n,m=map(int,input().split())
    b=[[0]*n for _ in'a'*n]
    b[n//2][n//2]=2
    b[n//2-1][n//2-1]=2
    b[n//2][n//2-1]=1
    b[n//2-1][n//2]=1
    for _ in'a'*m:
        i,j,c=map(int,input().split())
        f(i-1,j-1,c)
    aB=aW=0
    for i in b:
        aB+=i.count(1)
        aW+=i.count(2)
    print('#%i'%t,aB,aW)