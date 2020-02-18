# python3 시간 초과
# pypy3 통과

N = int(input())
L = [[0 for i in range(N)] for j in range(N)]
out = []
num = 0


def solve(depth, N, L):
    if N == 0:
        return 0
    if depth == N:
        global num
        num += 1
        return

    for i in range(N):
        if not L[depth][i]:
            for k in range(N):
                L[depth][k] += 1

            for j in range(depth + 1, N):
                L[j][i] += 1

            a = depth
            b = i
            while a != N - 1 and b != N - 1:
                a += 1
                b += 1
                L[a][b] += 1

            a = depth
            b = i
            while a != N - 1 and b != 0:
                a += 1
                b -= 1
                L[a][b] += 1

            out.append(1)

            solve(depth + 1, N, L)

            for k in range(N):
                L[depth][k] -= 1

            for j in range(depth + 1, N):
                L[j][i] -= 1

            a = depth
            b = i
            while a != N - 1 and b != N - 1:
                a += 1
                b += 1
                L[a][b] -= 1

            a = depth
            b = i
            while a != N - 1 and b != 0:
                a += 1
                b -= 1
                L[a][b] -= 1

            out.pop()


solve(0, N, L)

print(num)