import sys
sys.stdin=open('../input.txt','r')

def inorder_traverse(i,n):
    if 2*i<=n:
        inorder_traverse(2*i,n)
    tree[i]=k.pop()
    if 2*i+1<=n:
        inorder_traverse(2*i+1,n)

for t in range(1, int(input())+1):
    n=int(input())
    tree=[[]for _ in range(n+1)]
    k=list(range(n,0,-1))
    inorder_traverse(1,n)
    print('#%i'%t,tree[1],tree[n//2])