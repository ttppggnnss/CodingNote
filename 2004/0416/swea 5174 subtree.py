import sys
sys.stdin = open('../input.txt','r')

for t in range(1,int(input())+1):
    e,n=map(int,input().split())
    tree=[[] for _ in range(e+2)]
    data=[*map(int,input().split())]
    for i in range(e):
        tree[data[2*i]].append(data[2*i+1])
    q=[n]
    ans=0
    while q:
        a=q.pop()
        ans+=1
        q.extend(tree[a])
    print('#%i'%t, ans)