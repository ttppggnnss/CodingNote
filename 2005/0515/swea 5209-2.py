import sys
sys.stdin=open('../input.txt', 'r')

def bf(k, p):
    global ans
    if p>=ans:
        return
    if k==n:
        ans=min(ans,p)
        return
    for i in range(n):
        if v[i]<1:
            v[i]=1
            bf(k+1, p+board[k][i])
            v[i]=0

for t in range(1, int(input())+1):
    n = int(input())
    board = [[*map(int, input().split())] for _ in range(n)]
    v = [0]*n
    ans=9**9
    bf(0,0)
    print('#%i'%t, ans)