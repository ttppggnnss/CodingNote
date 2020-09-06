import sys
sys.stdin = open('../input.txt','r')

for t in range(1,int(input())+1):
    n, m, l = map(int,input().split())
    tree=[[] for _ in range(n+1)]
    for i in range(m):
        a,b=map(int,input().split())
        tree[a]=b
    for i in range(n,0,-1):
        if tree[i]==[]:
            try:
                tree[i]=tree[2*i]+tree[2*i+1]
            except:
                tree[i]=tree[2*i]
    print('#%i'%t,tree[l])