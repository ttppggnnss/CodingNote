# [문제 1] 스도쿠 게임

# 입력 테스트 용
# import sys
# sys.stdin = open('../input.txt', 'r')

# a 행과 b 열을 입력받아 체크한다
def check(a,b):
    # 총 3 가지를 체크해야한다
    # a 행
    box = sdoku[a]
    # b 열
    box2 = list([*zip(*sdoku)][b])
    # a 행 b 열 을 포함하는 3x3 사이즈의 박스
    a2 = a//3
    b2 = b//3
    box3 = []
    for i in range(3*a2,3*a2+3):
        for j in range(3*b2,3*b2+3):
            box3.append(sdoku[i][j])
    # 3가지를 각각 길이 9 의 리스트로 만들어서
    for k in range(1, 10):
        # 1~9 까지의 숫자 중 하나라도 2번 이상 반복되는 경우가 생긴다면 False 를 반환한다
        if box.count(k)>1 or box2.count(k)>1 or box3.count(k)>1:
            return False
    # 모든 경우에 반복되는 경우가 없다면 True 를 반환한다
    return True

# 테스트 케이스 개수를 입력받는다
for t in range(1, int(input())+1):
    # 입력 횟수 n 을 입력받는다
    n = int(input())
    # 초기 스도쿠 퍼즐을 입력받는다
    sdoku = [[*map(int, input().split())] for _ in range(9)]
    # 기준값을 만들어준다 (게임을 계속 할 것인지 넘길 것인지)
    std = 1
    # n 번 만큼 입력 받아야 한다
    for z in range(n):
        # 행 번호, 열 번호, 숫자 를 입력받고
        i, j, value = map(int, input().split())
        # 스도쿠 퍼즐에서 값을 넣어준다
        sdoku[i][j] = value
        # 게임을 게속 진행할 거라면
        if std:
            # i 행과 j 열 의 값을 함수에 넣어서 체크해준다
            if check(i, j) == False:
                # 반환 값이 False 라면 게임을 그만 둘 것이다
                # z 는 0 부터 시작했으므로 그만두는 번 째 값에서 1을 빼줄 필요가 없다
                print('#%i'%t, z)
                # 게임을 그만할 것이므로 기준 값을 바꿔준다
                # 게임을 그만둬도 n 번 만큼 입력받아야 한다
                std = 0
    # 게임을 끝까지 진행했다면 기준 값이 1 일 것이다
    if std:
        # 그럼 게임을 진행한 횟수 n 을 출력해준다
        print('#%i'%t, n)
