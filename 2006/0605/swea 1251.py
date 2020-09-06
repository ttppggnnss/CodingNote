import sys
sys.stdin=open('../input.txt', 'r')

# input()
# for t in range(1, 12):
for t in range(1, int(input())+1):
    n = int(input())
    data = []
    for _ in range(2):
        data.extend([*map(int, input().split())])

    e = float(input())

    V = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            V[i][j] = (data[j]-data[i])**2 + (data[n+j]-data[n+i])**2

    # print(V)

    ans = 0
    visit = [0] * n
    v = 0
    cnt = 1
    pq = [0]

    while cnt<n:
        minn = 10**12
        visit[v] = 1
        cnt += 1
        for i in pq:
            for j in range(n):
                if visit[j]<1 and V[i][j]<minn:
                    minn = V[i][j]
                    k2 = i
                    k = j
        v = k
        pq.append(v)
        ans += minn
        # print(e, k2, k, minn)
    print('#%i'%t, round(e*ans))
