import sys
sys.stdin=open('input.txt','r')
u=input
for t in range(1, int(u())+1):
    n, b = map(int,u().split())
    h=[*map(int,u().split())]
    mn=9**9
    i=0
    c=0
    while i+1:
        if c>=b:
            mn=c
            break
        if c==b:
            mn=b
            break
        if c<b:
            c+=h[i]
        if c<b:
            pass
        i+=1

    print('#%i'%t,mn-b)