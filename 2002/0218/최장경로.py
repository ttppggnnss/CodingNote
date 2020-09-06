import sys
sys.stdin=open('최장경로.txt','r')

def linked(i, Visited, L,L2):
    global ans
    Visited[i] = 1
    L2.append(i)
    start = 0
    for j in range(L[i].count(1)):
        start = L[i].index(1, start)
        if L[i][start]>0 and Visited[start]==0:
            L[i][start]=0
            L[start][i]=0
            linked(start, Visited, L, L2)
            L[i][start]=1
            L[start][i]=1
    if ans<len(L2):ans=len(L2)
    return

for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    L = [[0] * n for _ in [0] * n]
    for _ in [0] * m:
        x, y = map(int, input().split())
        L[x - 1][y - 1] = 1
        L[y - 1][x - 1] = 1
    Visited = [0] * n
    ans=0
    for i in range(n):
        L2 = []
        linked(i, Visited, L,L2)
    print('#%d' % t,ans)