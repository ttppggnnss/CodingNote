import sys
from itertools import permutations as p
n=int(sys.stdin.readline())
I=[[*map(int,input().split())]for _ in'a'*n]
ans=0

def g(l):
    cnt=0
    score=0
    for i in I:
        out=0
        b1,b2,b3=0,0,0
        while out<3:
            if i[l[cnt]]==0:out+=1
            if i[l[cnt]]==1:score+=b3;b1,b2,b3=1,b1,b2
            if i[l[cnt]]==2:score+=b2+b3;b1,b2,b3=0,1,b1
            if i[l[cnt]]==3:score+=b1+b2+b3;b1,b2,b3=0,0,1
            if i[l[cnt]]==4:score+=b1+b2+b3+1;b1,b2,b3=0,0,0
            cnt=(cnt+1)%9
    return score

for l in p(range(1,9),8):
    l=list(l)
    l.insert(3,0)
    ans=max(ans,g(l))
print(ans)