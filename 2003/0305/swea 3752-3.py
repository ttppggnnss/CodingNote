# 비트 마스킹
# 시간 초과
import sys
sys.stdin=open('input.txt','r')

for t in range(1,1+int(input())):
    n=int(input())
    score=[*map(int,input().split())]
    v=[1]+[0]*sum(score)
    for i in range(1<<n):
        s=0
        for j in range(n):
            if i&(1<<j):
                s+=score[j]
                v[s]=1
    print('#%i'%t,sum(v))
