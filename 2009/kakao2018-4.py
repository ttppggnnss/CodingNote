# 프렌즈 4블록
# 2020/09/10 21:50 ~ 22:20

import sys
sys.stdin=open('./input.txt', 'r')

# 입력값
#       m	n	board	                                                        answer
ex1 =   4,	5,	['CCBDE', 'AAADE', 'AAABF', 'CCBBF']	                        # 14
ex2 =   6,	6,	['TTTANT', 'RRFACC', 'RRRFCC', 'TRRRAA', 'TTMMMF', 'TMMTTJ']	# 15
ex3 =   6,  6,  ['AAAAAA', 'BBAATB', 'BBAATB', 'BBAATB', 'JJJTAA', 'JJJTAA']    # 28

# 풀이 설계
# 1. 높이 m, 폭 n 을 입력 받는다. 전체를 F 로 설정한다
# 2. 블록을 순회하며 (각각 m-1, n-1 까지) 2x2 를 찾아서 일치하면 T 로 바꿔준다
# 3. T 를 제외하고 블록 값을 '' 빈 문자열로 바꿔준다
# 4. 세로방향 아래로 빈 문자열인 경우 블럭을 밀어준다
# 5. 2번을 반복한다
# 6. 지워지는 블록 개수를 센다

def solution(m, n, board):
    answer = 0

    new_board = [[char for char in line] for line in board]
    board_boolean = [[False] * n for _ in range(m)]

    while True:
        # for i in new_board:
        #     print(*i)
        # print('\n')

        check_new_board = [[el for el in line] for line in new_board]

        for i in range(m - 1):
            for j in range(n - 1):
                if new_board[i][j] == new_board[i + 1][j] and new_board[i][j] == \
                        new_board[i][j + 1] and new_board[i][j] == new_board[i + 1][j + 1]:
                    board_boolean[i][j] = board_boolean[i + 1][j] = board_boolean[i][j + 1] = board_boolean[i + 1][
                        j + 1] = True

        for i in range(m):
            for j in range(n):
                if new_board[i][j] != '0' and board_boolean[i][j] == True:
                    new_board[i][j] = '0'

        for i in range(m - 1, 0, -1):
            for j in range(n - 1, -1, -1):
                i2 = i
                while i2 > 0:
                    if new_board[i2][j] == '0':
                        new_board[i2][j], new_board[i2 - 1][j] = new_board[i2 - 1][j], new_board[i2][j]

                    if board_boolean[i2][j] == True:
                        board_boolean[i2][j], board_boolean[i2 - 1][j] = board_boolean[i2 - 1][j], board_boolean[i2][j]

                    i2 -= 1

        if new_board == check_new_board:
            break

    for i in range(m):
        for j in range(n):
            if board_boolean[i][j] == True:
                answer += 1

    return answer



print(solution(*ex3))
# answer = 0
#
# new_board = [[char for char in line] for line in board]
# board_boolean = [[False]*n for _ in range(m)]
#
#
# for i in range(m-1):
#     for j in range(n-1):
#         if new_board[i][j] == new_board[i+1][j] and new_board[i][j] == new_board[i][j+1] and new_board[i][j] == new_board[i+1][j+1]:
#             board_boolean[i][j] = board_boolean[i+1][j] = board_boolean[i][j+1] = board_boolean[i+1][j+1] = True
#
# for i in range(m):
#     for j in range(n):
#         if new_board[i][j] != '' and board_boolean[i][j] == True:
#             new_board[i][j] = ''
#
# print(new_board)
# for i in range(m-1, 0, -1):
#     for j in range(n-1, -1, -1):
#         i2 = i
#         while i2>0:
#             if new_board[i2][j] == '':
#                 new_board[i2][j], new_board[i2-1][j] = new_board[i2-1][j], new_board[i2][j]
#
#             if board_boolean[i2][j] == True:
#                 board_boolean[i2][j], board_boolean[i2-1][j] = board_boolean[i2-1][j], board_boolean[i2][j]
#
#             i2 -= 1
#
# print(new_board)
# print(board_boolean)