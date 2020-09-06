import sys
sys.stdin=open('../input.txt', 'r')

def f(b,c,h):
    if c>=b:
        ans.append(c)
    for i,x in enumerate(h):
        c+=x
        h2=h[i+1:]
        f(b,c,h2)
        c-=x

for t in range(1, int(input())+1):
    n, b = map(int,input().split())
    h=[*map(int,input().split())]
    ans=[]
    f(b,0,h)
    print(ans)
    print('#%i'%t,min(ans)-b)