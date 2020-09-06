# 시간 초과
import sys
sys.stdin=open('input.txt','r')
from itertools import combinations as c
for t in range(1,1+int(input())):
    n=int(input())
    score=[*map(int,input().split())]
    ans={0}
    for i in range(1,n+1):
        for j in c(score,i):
            ans.add(sum(j))
    print('#%i'%t,len(ans))
