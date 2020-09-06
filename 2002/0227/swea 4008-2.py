import sys
sys.stdin=open('input.txt','r')

def f(m, i, a, b, c, d):
    global n, mx, mn
    if i==n:
        mx=max(m,mx)
        mn=min(m,mn)
        return
    else:
        if a:
            f(m+N[i],i+1,a-1,b,c,d)
        if b:
            f(m-N[i],i+1,a,b-1,c,d)
        if c:
            f(m*N[i],i+1,a,b,c-1,d)
        if d:
            if m>0:
                f(m//N[i],i+1,a,b,c,d-1)
            else:
                f(-((-m)//N[i]),i+1,a,b,c,d-1)
for t in range(1,int(input())+1):
    n=int(input())
    a,b,c,d=map(int,input().split())
    N=[*map(int,input().split())]
    mx=-9**9
    mn=9**9
    f(N[0],1,a,b,c,d)
    print('#%i'%t,mx-mn)