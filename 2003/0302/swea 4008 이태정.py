operator = ['+', '-', '*', '/']

def calculation(R, C, S):  # 계산
    if S == '+':
        return R + C
    elif S == '-':
        return R - C
    elif S == '*':
        return R * C
    else:
        return int(R / C)


def getresult():
    global max_result, min_result, N
    result = card[0]  # 맨 처음 카드놓고
    for y in range(1, N):
        result = calculation(result, card[y], stack[y - 1])
    if result > max_result:
        max_result = result
    if result < min_result:
        min_result = result


def OP():  # 스택활용
    if len(stack) == N - 1:
        getresult()

    else:
        for y in range(4):
            if operator_cnt[y]:
                stack.append(operator[y])
                operator_cnt[y] -= 1
                OP()

                stack.pop()
                operator_cnt[y] += 1


T = int(input())
for i in range(1, T + 1):
    N = int(input())
    operator_cnt = list(map(int, input().split()))
    card = list(map(int, input().split()))
    max_result = -100000000
    min_result = 100000000
    stack = []
    OP()
    print('#{} {}'.format(i, max_result - min_result))