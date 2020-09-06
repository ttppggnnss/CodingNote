import sys
sys.stdin=open('../input.txt', 'r')
input = sys.stdin.readline
n, s, m = map(int, input().split())
V =[*map(int, input().split())]
dp = [s]
for i in V:
    dp = set([j+i for j in dp if j+i<=m]+[j-i for j in dp if j-i>=0])
    if not dp:print(-1)
print(max(dp))