# 숏코딩
import sys
sys.stdin=open('input.txt','r')

for t in range(1,11):
    v,s=map(int,input().split())
    c=[*map(int,input().split())]
    V=[[]for i in'a'*101]
    q=[[s]]
    p=[0]*101
    p[s]=1
    for i in range(v//2):
        V[c[2*i]]+=[c[2*i+1]]
    while q[-1]:
        q+=[[]]
        for i in q[-2]:
            for j in V[i]:
                if p[j]<1:
                    q[-1]+=[j]
                    p[j]=1
    print('#%d'%t,max(q[-2]))