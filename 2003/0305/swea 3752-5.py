# 시간 초과
import sys
sys.stdin=open('input.txt','r')

for t in range(1,1+int(input())):
    n=int(input())
    sco=[*map(int,input().split())]
    ans=[0]
    for i in sco:
        for j in range(len(ans)):
            ans.append(ans[j]+i)
    print('#%i'%t,len(set(ans)))
