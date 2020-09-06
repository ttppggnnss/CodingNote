import sys
sys.stdin=open('input.txt','r')

for t in range(1,int(input())+1):
    N,A,B=map(int,input().split())
    ans=10**10
    for R in range(1,N//2+1):
        for C in range(N//R,N//R-2,-1):
            if ans>A*abs(R-C)+B*(N-R*C):
                ans=A*abs(R-C)+B*(N-R*C)
    print('#%i'%t,ans)