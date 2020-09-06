# 숏코드
def back(k, f, u):
    global Max
    if Max >= f: return
    if k == N: Max = max(Max, f);return;
    for i in range(N):
        if not (u & 2 ** i): back(k + 1, f * p[i][k] / 100, u + 2 ** i)


for t in range(1, int(input()) + 1):
    N = int(input())
    p = [list(map(int, input().split())) for _ in range(N)]
    Max = 0
    back(0, 1.0, 0)
    print("#{} {:.6f}".format(t, Max * 100))
