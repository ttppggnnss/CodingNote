import sys
sys.stdin=open('../input.txt','r')

L=['1','2','3']
def f(n,c='',k=0):
    global p
    if len(p):
        return
    if k==n:
        p.append(c)
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
    for i in range(k):
        for j in range(i+1,k+1):
            s2=d[i:j]
            m=(j-i+1)//2
            if s2[:m]==s2[m:]:
                return False
    return True
p=[]
f(int(input()))
print(p[0])