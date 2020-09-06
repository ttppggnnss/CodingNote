import sys
sys.stdin=open('../input.txt', 'r')

def DC(k,l,r, flag):
    if l > r:
        return 0
    m = (l+r)//2
    if A[m]==k:
        return 1
    elif A[m]>k:
        if flag==-1:
            return 0
        else:
            return DC(k, l, m-1, -1)
    else:
        if flag==1:
            return 0
        else:
            return DC(k, m+1, r, 1)

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    A = sorted([*map(int, input().split())])
    B = [*map(int, input().split())]
    ans=0
    for i in B:
        ans+=DC(i,0,N-1,0)
    print('#%i'%tc,ans)