# [문제 3] 런닝 싸피맨

# 입력 테스트 용
import sys
sys.stdin = open('../input.txt', 'r')

# 2 에서 2로 가는 길 중 최단 거리를 구하는 것과 비슷하게 생각할 수 있다
# 양쪽에서 출발하므로 2로 나눠주면 되는데
# 주의해야 하는 것은 둘이 동시에 문을 통과하면 안된다는 것이다
# 그러므로 전체 길이에서 1을 더해주고 2로 나눈 몫을 계산해주면 된다

# 4방향으로 가는 길을 선언해주고
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
# 최단 거리에 1 을 더해서 반환해주는 함수를 선언한다
def solve(a):
    # 갔던길 반복하지 않으려고 visit 를 설정한다
    visit = [[0]*n for _ in range(n)]
    # 가는 지점들을 기억해둘 저장소를 선언해준다
    q = [a]
    # 거리 값을 선언해준다
    cnt = 0
    # 지점들이 있는 동안
    while q:
        # 거리에 1을 더해주고
        cnt += 1
        # 현재 q 에 있는 지점들 개수만큼
        for _ in range(len(q)):
            # 제일 앞에 있는 값을 빼준다
            i, j = q.pop(0)
            # 방문표시를 하고
            visit[i][j] = 1
            # 동서남북 4 방위에 대해서
            for k in range(4):
                ni, nj = i+di[k], j+dj[k]
                # room 안에 있는 값이고 갈 수 없는 1 이 아니면서 방문한 적이 없으면
                if -1<ni<n and -1<nj<n and visit[ni][nj]<1 and room[ni][nj]!=1:
                    # q 에 뒤쪽에 저장해준다
                    q.append((ni, nj))
                    # 만약 저장해주는 값이 2라면
                    if room[ni][nj]==2:
                        # 현재 거리에서 1을 더해서 반환해준다
                        return cnt+1
# n 을 입력받는다
n = int(input())
# 출발 후보지 리스트를 선언한다
start = []
# n x n 방을 입력받는다
room = []
for i in range(n):
    room.append([*map(int, input().split())])
    for j in range(n):
        # 출발 후보지 위치를 저장한다
        if room[i][j]==2:
            start.append((i,j))
# 최소값을 선언한다
ans = 9**9
# 출발지마다
for i in start:
    # solve 로 거리를 계산해 준 다음
    res = solve(i)
    # 최소값인 경우 값을 저장한다
    ans = min(ans, res//2)
# 저장된 최소값을 출력한다
print(ans)