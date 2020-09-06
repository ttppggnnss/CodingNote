# 숏코딩 도전
from itertools import permutations as p
u=input;n=int(u());a=0;I=[[*map(int,u().split())]for _ in'a'*n]
for l in p(range(1,9),8):
    l=list(l);l.insert(3,0);c=0;s=0
    for i in I:
        out=0;x,y,z=0,0,0
        while out<3:
            k=i[l[c]]
            if k==0:out+=1
            if k==1:s+=z;x,y,z=1,x,y
            if k==2:s+=y+z;x,y,z=0,1,x
            if k==3:s+=x+y+z;x,y,z=0,0,1
            if k==4:s+=x+y+z+1;x,y,z=0,0,0
            c=(c+1)%9
    a=max(a,s)
print(a)