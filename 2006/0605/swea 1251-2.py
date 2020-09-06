import sys
sys.stdin=open('../input.txt', 'r')

import heapq

for t in range(1, int(input())+1):
    n = int(input())
    data = []
    for _ in range(2):
        data.extend([*map(int, input().split())])
    e = float(input())
    ans = 0
    visit = [0] * n
    cnt = 0
    pq = []
    heapq.heappush(pq, (0,0))
    while cnt<n:
        val, i = heapq.heappop(pq)
        while visit[i]:
            val, i = heapq.heappop(pq)
        visit[i] = 1
        cnt += 1
        for j in range(n):
            if visit[j]<1:
                heapq.heappush(pq, ((data[j]-data[i])**2 + (data[n+j]-data[n+i])**2, j))
        ans += val
    print('#%i'%t, round(e*ans))
