import sys
sys.stdin=open('input.txt', 'r')

def f(s,g):
    a=g[0]-s[0];b=g[1]-s[1]
    if a>0 and b>0:return max(a,b)
    elif a<0 and b<0: return max(abs(a),abs(b))
    else:return abs(a)+abs(b)
for t in range(1,int(input())+1):
    w,h,n=map(int,input().split());ans=0
    s=[*map(int,input().split())]
    for _ in 'a'*(n-1):g=[*map(int,input().split())];ans+=f(s,g);s=g
    print('#%i'%t, ans)