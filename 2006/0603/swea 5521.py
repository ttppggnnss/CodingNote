import sys
sys.stdin=open('../input.txt', 'r')

for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    V = [[] for _ in range(n+1)]
    for i in range(m):
        a, b = map(int, input().split())
        V[a].append(b)
        V[b].append(a)
    q = [1]
    cnt = -1
    visit = [0]*(n+1)
    k=3
    while k:
        for _ in range(len(q)):
            v = q.pop(0)
            if visit[v]<1:
                cnt+=1
                visit[v]=1
                for i in V[v]:
                    if visit[i]<1:
                        q.append(i)
        k-=1
    print('#%i'%t, cnt)