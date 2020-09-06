import sys
sys.stdin=open('input.txt','r')

def maze(st):
    global cnt
    j,i=st
    for dj,di in (1,0),(0,1),(-1,0),(0,-1):
        nj,ni=j+dj,i+di
        if 0<=nj<n and 0<=ni<n:
            if L[nj][ni]==3:
                global ans
                ans=cnt
            if L[nj][ni]==0:
                L[nj][ni]=1
                cnt+=1
                maze((nj,ni))
                L[nj][ni]=0
                cnt-=1

for t in range(1,int(input())+1):
    n=int(input())
    L=[]
    for i in range(n):
        L.append([*map(int,input())])
        if 2 in L[-1]:
            st=(i,L[-1].index(2))
    cnt=0
    ans=0
    maze(st)
    print('#%i'%t,ans)