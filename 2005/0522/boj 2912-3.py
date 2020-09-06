# 하
import sys
sys.stdin=open('../input.txt', 'r')
# sys.setrecursionlimit(9**9)

def f(l, r, i):
    if r-l==1:
        if hat[l]==i:
            return 1
        else:
            return 0
    c = (r+l)//2
    left = f(l,c,i)
    right = f(c,r,i)
    return left+right

n, c = map(int, input().split())
hat = [*map(int, input().split())]
m = int(input())
for _ in range(m):
    s, e = map(int, input().split())
    z = (e-s+1)//2
    j=0
    for i in range(1,c+1):
        if j>z:
            continue
        cal = f(s-1,e,i)
        j+=cal
        if cal>z:
            print('yes', i)
            break
    else:
        print('no')

