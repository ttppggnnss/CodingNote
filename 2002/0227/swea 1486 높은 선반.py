import sys
sys.stdin=open('input.txt','r')

def f(b,c,h):
    global mn
    if c>=0:
        mn=min(c,mn)
        return
    for i,x in enumerate(h):
        c+=x
        h2=h[i+1:]
        f(b,c,h2)
        c-=x

for t in range(1, int(input())+1):
    n, b = map(int,input().split())
    h=[*map(int,input().split())]
    mn=9**9
    f(b,-b,h)
    print('#%i'%t,mn)