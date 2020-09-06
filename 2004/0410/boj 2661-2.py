import sys
sys.stdin=open('../input.txt','r')

L=['1','2','3']
def f(n,c='',k=0):
    global p
    if p:
        return
    if k==n:
        p=c
        print(p)
        return
    else:
        for i in L:
            d=c+i
            if g(d):
                f(n,d,k+1)
            else:
                continue
def g(d):
    k=len(d)
    m=(k+1)//2
    for i in range(2,m+2):
        if d[-1:-i:-1]==d[-i:-i-i+1:-1]:
            return False
    return True
p=0
f(int(input()))