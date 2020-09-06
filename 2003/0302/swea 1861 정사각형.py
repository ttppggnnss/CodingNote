import sys
sys.stdin=open('input.txt','r')

for t in range(1,1+int(input())):
    n=int(input())
    L=[[*map(int,input().split())] for _ in'a'*n]
    V=[[0]*n for _ in'a'*n]
    a,b=0,0
    h=1
    for i in range(n):
        for j in range(n):
            if V[i][j]<1:
                k=1
                s=i,j
                p=[(i,j)]
                while p:
                    i,j=p.pop()
                    for d,e in (1,0),(-1,0),(0,1),(0,-1):
                        I,J=i+d,j+e
                        if 0<=I<n and 0<=J<n and L[I][J]==L[i][j]+1:
                            V[I][J]=1
                            p.append((I,J))
                            k+=1
                if h<k:
                    h=k
                    a,b=s
                elif h==k:
                    if L[i][j]<L[a][b]:
                        a,b=s
    print('#%i'%t,L[a][b],h)