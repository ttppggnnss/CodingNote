import sys
sys.stdin=open('../input.txt','r')

for t in range(1, int(input())+1):
    n=int(input())
    tree=[[]for _ in range(n+1)]
    data=[*map(int,input().split())]
    for i in range(1,n+1):
        tree[i]=data[i-1]
        while 1:
            if i//2>0 and tree[i]<tree[i//2]:
                tree[i],tree[i//2]=tree[i//2],tree[i]
                i=i//2
            else:
                break
    ans=0
    while 1:
        n=n//2
        ans+=tree[n]
        if n==1:
            break
    print('#%i'%t, ans)