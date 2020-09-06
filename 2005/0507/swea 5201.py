import sys
sys.stdin=open('../input.txt', 'r')

for t in range(1, int(input())+1):
    n,m=map(int,input().split())
    W=sorted([*map(int,input().split())])
    T=sorted([*map(int,input().split())],reverse=True)
    ans=0
    for i in T:
        while W:
            a=W.pop()
            if a<=i:
                ans+=a
                break
    print('#%i'%t, ans)