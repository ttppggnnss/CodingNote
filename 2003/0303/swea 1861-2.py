import sys
sys.stdin=open('input.txt','r')

for t in range(1,1+int(input())):
    n=int(input())
    L=[[*map(int,input().split())] for _ in'a'*n]
    V=[0]*(n**2+1)
    for i in range(n):
        for j in range(n):
                for di,dj in (1,0),(-1,0),(0,1),(0,-1):
                    if -1<i+di<n and -1<j+dj<n and L[i+di][j+dj]==L[i][j]+1:
                        V[L[i][j]]=1
                        break
    a,b,c=1,0,1
    for i in range(n**2+1):
        if V[i]==1:c+=1
        else:
            if c>a:a=c;b=i+1-c
            c=1
    print('#%i'%t,b,a)