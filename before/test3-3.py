# 실행시간 # 백준 시간초과

def f(i, N):
    global cnt
    if i == N:
        cnt += 1
    else:
        for j in range(N):
            if col[j] == 0 and del_right[i + N - 1 - j] == 0 and del_left[i + j] == 0:
                col[j] = 1
                del_right[i + N - 1 - j] = 1
                del_left[i + j] = 1

                f(i + 1, N)

                col[j] = 0
                del_right[i + N - 1 - j] = 0
                del_left[i + j] = 0


N = int(input())
arr = [[0 for i in range(N)] for i in range(N)]
col = [0 for i in range(N)]
del_right = [0 for i in range(2 * N - 1)]
del_left = [0 for i in range(2 * N - 1)]
cnt = 0
f(0, N)
print(cnt)