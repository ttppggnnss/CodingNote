# 실행시간
import sys
sys.stdin=open('input.txt', 'r')

from collections import deque

def dfs(x, y):
    global K, info
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    visited = [0] * N * N
    s = deque()
    visited[x * N + y] = 1
    s.append((x, y, 1, 0, info[x][y], visited))  # x, y, 등산로 수, 중복 공사를 피하기 위한 flag, 현재 위치의 높이, 방문 정보
    result = 0
    while s:
        x_, y_, cnt, flag, now, visited = s.pop()
        if result < cnt:  # cnt가 result보다 높으면 갱신
            result = cnt
        for k in range(4):
            ni = x_ + di[k]
            nj = y_ + dj[k]
            if 0 <= ni < N and 0 <= nj < N and now > info[ni][nj] and visited[ni * N + nj] == 0:  # 다음으로 나갈 수 있으면
                visited[ni * N + nj] = 1
                s.append((ni, nj, cnt + 1, flag, info[ni][nj], visited[:]))  # flag와 다음 위치를 stack에 저장
                visited[ni * N + nj] = 0
            elif not flag and 0 <= ni < N and 0 <= nj < N and now > info[ni][nj] - K and visited[
                ni * N + nj] == 0:  # 공사를 한 번도 안했고, 최대 공사 가능 깊이를 뺐을 경우 now보다 작다면
                for cut in range(1, K + 1):  # 1부터 최대 공사 가능 높이까지 하나씩 현재 위치에서 빼면서 비교
                    if now > info[ni][nj] - cut:  # 현재값이 다음위치-공사높이보다 크다면 진행
                        visited[ni * N + nj] = 1
                        s.append((ni, nj, cnt + 1, 1, info[ni][nj] - cut, visited[:]))  # flag를 1로 표시하여 공사 진행 표시
                        visited[ni * N + nj] = 0
    return result


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(N)]
    maxH = 0
    maxV = 0
    for i in range(N * N):  # 최대 높이 찾기
        if maxH < info[i // N][i % N]:
            maxH = info[i // N][i % N]
    for i in range(N):
        for j in range(N):
            if info[i][j] == maxH:  # 최대 높이 좌표를 찾으면 dfs 돌리기
                answer = dfs(i, j)
                if maxV < answer:
                    maxV = answer
    print('#{0} {1}'.format(tc, maxV))