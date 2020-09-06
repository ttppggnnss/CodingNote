import sys
sys.stdin=open('../input.txt', 'r')

def bf(v, k, p):
    if k==n:
        global ans
        ans=min(ans,sum(p))
        return
    for i in range(n):
        if v[i]<1:
            v[i]=1
            p.append(board[k][i])
            bf(v[:], k+1, p[:])
            v[i]=0
            p.pop()

for t in range(1, int(input())+1):
    n = int(input())
    board = [[*map(int, input().split())] for _ in range(n)]
    v = [0]*n
    ans=9**9
    bf(v,0,[])
    print('#%i'%t, ans)