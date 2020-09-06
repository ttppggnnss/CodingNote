import sys
sys.stdin=open('../input.txt', 'r')

import heapq

for t in range(1, int(input())+1):
    v, e = map(int, input().split())
    adj = {i :[] for i in range(v+1)}
    visit = [0]*(v+1)
    for _ in range(e):
        n1, n2, w = map(int, input().split())
        adj[n1].append([n2,w])
        adj[n2].append([n1,w])
    key = [10e9]*(v+1)
    mst = [0]*(v+1)
    heap = []
    key[0]=0
    heapq.heappush(heap,(key[0],0))
    while heap:
        k, node = heapq.heappop(heap)
        mst[node]=1
        for dest, wt in adj[node]:
            if mst[dest]<1 and key[dest]>wt:
                key[dest] = wt
                heapq.heappush(heap, (key[dest], dest))
    print('#%i'%t, sum(key))