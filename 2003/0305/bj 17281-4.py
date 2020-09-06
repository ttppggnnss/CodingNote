# 그나마 최단 시간
from itertools import permutations

N = int(input())
P = [[0] * 9] + [[0] + list(map(int, input().split())) for _ in range(N)]
max_score = -1

for perm in permutations(range(2, 10)):
    arr = [0] + list(perm)[:3] + [1] + list(perm)[3:]

    score = 0
    num = 1
    for inning in range(1, N + 1):
        r1, r2, r3 = 0, 0, 0
        out = 0
        while True:
            if out == 3:
                break
            p = P[inning][arr[num]]
            if p == 0:
                out += 1

            elif p == 1:
                score += r3
                r1, r2, r3 = 1, r1, r2

            elif p == 2:
                score += r2 + r3
                r1, r2, r3 = 0, 1, r1

            elif p == 3:
                score += r1 + r2 + r3
                r1, r2, r3 = 0, 0, 1

            elif p == 4:
                score += r1 + r2 + r3 + 1
                r1, r2, r3 = 0, 0, 0

            if num == 9:
                num = 1
            else:
                num += 1
    if score > max_score:
        max_score = score

print(max_score)