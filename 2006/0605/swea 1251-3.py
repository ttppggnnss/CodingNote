# 성환이 방법 참고
import sys
sys.stdin=open('../input.txt', 'r')

for t in range(1, int(input()) + 1):
    n = int(input())
    xs = [*map(int, input().split())]
    ys = [*map(int, input().split())]
    e = float(input())

    v = 0
    val = [10 ** 12] * n
    visit = [0] * n
    val[v] = 0
    for _ in range(n):
        visit[v] = 1
        min_idx = -1
        min_val = 10 ** 12
        for i in range(n):
            dist = (xs[i] - xs[v]) ** 2 + (ys[i] - ys[v]) ** 2
            if visit[i] < 1 and dist < val[i]:
                val[i] = dist
        for idx, k in enumerate(val):
            if visit[idx] < 1 and k < min_val:
                min_val, min_idx = k, idx
        v = min_idx

    print('#%i'%t, round(e * sum(val)))