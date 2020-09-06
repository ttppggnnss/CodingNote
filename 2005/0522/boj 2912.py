# 시간초과
import sys
sys.stdin=open('../input.txt', 'r')

n, c = map(int, input().split())
hat = [*map(int, input().split())]
m = int(input())
for _ in range(m):
    s, e = map(int, input().split())
    colors={}
    for i in range(1,c+1):
        try:
            colors[i]=hat[s-1:e].count(i)
        except:
            pass
    for i,j in colors.items():
        if j>(e-s+1)//2:
            print('yes', i)
            break
    else:
        print('no')
