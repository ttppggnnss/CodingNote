import sys
sys.stdin=open('../input.txt', 'r')

for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    V = [[] for _ in range(n+1)]
    for i in range(m):
        a, b = map(int, input().split())
        V[a].append(b)
        V[b].append(a)
    cnt = set([1]) | set(V[1])
    for i in V[1]:
        cnt|=set(V[i])
    print('#%i'%t, len(cnt)-1)