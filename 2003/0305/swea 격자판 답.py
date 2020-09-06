T = int(input())

def find(i, j, n, s):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    if (n == 7):
        t.add(s)
    else:
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if (ni >= 0 and ni < 4 and nj >= 0 and nj < 4):
                find(ni, nj, n + 1, s + a[i][j])

for tc in range(1, T + 1):
    a = [list(input().split()) for i in range(4)]
    t = set()
    for i in range(4):
        for j in range(4):
            find(i, j, 0, '')
    print('#{} {}'.format(tc, len(t)))