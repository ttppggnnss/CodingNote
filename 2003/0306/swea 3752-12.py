import sys
sys.stdin=open('input.txt', 'r')
# 시간초과
# idea 6???
u=input
for t in range(1,1+int(u())):
    u();s=[*map(int,u().split())];v=[0]*sum(s)+[1]
    for i in s:
        for j in range(sum(s)+1):
            v2=v[:]
            if v[j]:v2[j-i]=1
            v=v2[:]
    print('#%i'%t,sum(v))