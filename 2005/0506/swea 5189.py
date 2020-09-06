import sys
sys.stdin=open('../input.txt', 'r')

from itertools import permutations as p

for t in range(1, int(input())+1):
    n=int(input())
    board=[[*map(int,input().split())] for _ in range(n)]
    ans=9**9
    candi=p(range(1,n), n-1)
    for i in candi:
        res=0
        i=[0]+list(i)+[0]
        for j in range(n):
            res+=board[i[j]][i[j+1]]
        ans=min(res,ans)
    print('#%i'%t, ans)