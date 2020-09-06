# 숏코딩
T = int(input())
for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    flag = [list(input()) for _ in range(N)]
    check = 1000000
    w, b, r = 0, 0, 0

    for i in range(0, N - 2):
        w += M - flag[i].count('W')
        b = w
        for j in range(i + 1, N - 1):
            b += M - flag[j].count('B')
            r = b
            for k in range(j + 1, N):
                r += M - flag[k].count('R')
            check = min(check, r)
    print('#{} {}'.format(tc, check))