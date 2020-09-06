# 시간초과
import sys
sys.stdin=open('../input.txt', 'r')

n, c = map(int, input().split())
hat = [*map(int, input().split())]
colors = {i:[] for i in range(1, c+1)}
for i in range(n):
    colors[hat[i]].append(i)
m = int(input())
for _ in range(m):
    s, e = map(int, input().split())
    z = (e-s+1)//2
    for i in range(1,c+1):
        a = [z for z in colors[i] if s-1<=z and z<e]
        if len(a)>z:
            print('yes', i)
            break
    else:
        print('no')

