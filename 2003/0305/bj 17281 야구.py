# 시간초과
import sys
sys.stdin=open('input.txt','r')
from itertools import permutations as p

n=int(sys.stdin.readline())
b=[[*map(int,sys.stdin.readline().split())]for _ in'a'*n]
ans=0

for i in p(range(1,9),8):
    i=list(i)
    i.insert(3,0)
    c=0
    inn=0
    score=0
    while inn<n:
        out=0
        b1,b2,b3=0,0,0
        while out<3:
            if b[inn][i[c]]==0:
                out+=1
            if b[inn][i[c]]==1:
                score+=b3
                b1,b2,b3=1,b1,b2
            if b[inn][i[c]]==2:
                score+=b2+b3
                b1,b2,b3=0,1,b1
            if b[inn][i[c]]==3:
                score+=b1+b2+b3
                b1,b2,b3=0,0,1
            if b[inn][i[c]]==4:
                score+=b1+b2+b3+1
                b1,b2,b3=0,0,0
            c=(c+1)%9
        inn+=1
    ans=max(ans,score)
print(ans)



