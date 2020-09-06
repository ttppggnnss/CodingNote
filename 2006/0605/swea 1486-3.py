# 숏코딩
import sys
sys.stdin=open('../input.txt', 'r')
u=input;I=int;s=set
for t in range(1, I(u())+1):
    n,b=map(I,u().split());h=[*map(I,u().split())];r=s()
    for i in h:r |= s(j+i for j in r);r.add(i)
    print('#%i'%t,min(i for i in r if i>=b)-b)