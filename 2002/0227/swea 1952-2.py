import sys
sys.stdin=open('input.txt','r')

def f(i):
    global suma,ans
    if i>=12:
        ans=min(ans,suma)
    else:
        if plan[i]==0:
            f(i+1)
        if i<12:
            suma+=c
            f(i+3)
            suma-=c
        if i<12:
            suma+=b
            f(i+1)
            suma-=b
        if i<12:
            suma+=a*plan[i]
            f(i+1)
            suma-=a*plan[i]

for t in range(1,int(input())+1):
    a, b, c, d=map(int,input().split())
    plan=[*map(int,input().split())]
    suma=0
    ans=d
    f(0)
    print('#%i'%t,ans)