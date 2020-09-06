import sys
sys.stdin=open('../input.txt','r')

import sys
sys.setrecursionlimit(10**8)
input=sys.stdin.readline

def solve1(i):
    a,b=i
    if a==1:
        return b
    else:
        return b+solve1(tree[a][0])

def solve2(i,j):
    a,b=i
    c,d=j
    if a==c:
        return b+d
    else:
        if a>c:
            a,c=c,a
            b,d=d,b
        return d+solve2([a,b],tree[c][0])

n=int(input())
tree=[[] for i in range(n+1)]

for i in range(n-1):
    a,b,c=map(int,input().split())
    tree[a].append([b,c])
    tree[b].append([a,c])

candi=[i for i in tree if len(i)==1]

candi2=[solve1(i[0]) for i in candi]
a=candi2.index(max(candi2))

ans=0
for i in range(len(candi)):
        res=solve2(candi[i][0],candi[a][0])
        ans=max(res,ans)
print(ans)
