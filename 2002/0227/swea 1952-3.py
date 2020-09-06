import sys
sys.stdin=open('input.txt','r')

u=input
q=lambda:map(int,u().split())
for T in range(*q()):
    D,M,Q,Y=q()
    P,i=[*q()],11
    m=[min(M,D*p)for p in P]+[0]*3
    while i>-1:
        m[i]=min(m[i]+m[i+1],Q+m[i+3])
        i-=1
    print('#%i'%(T+1),min(Y,m[0]))