import sys
sys.stdin = open('../input.txt','r')

for t in range(1,int(input())+1):
    N, M = map(int,input().split())
    a=input().split()
    for _ in range(M):
        a.append(a.pop(0))
    print('#%i'%t, a[0])