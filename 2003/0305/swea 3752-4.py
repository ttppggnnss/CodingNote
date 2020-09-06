# 비트 마스킹
# 시간 초과
import sys
sys.stdin=open('input.txt','r')

for t in range(1,1+int(input())):
    n=int(input())
    score=[*map(int,input().split())]
    a=sum(score)//2
    v=[1]+[0]*a
    for i in range(1<<n):
        s=0
        for j in range(n):
            if i&(1<<j):
                s+=score[j]
                if s>a:break
                else:v[s]=1
    print('#%i'%t,sum(v)+sum(v[:-1]))
