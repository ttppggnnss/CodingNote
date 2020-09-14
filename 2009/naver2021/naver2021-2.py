# 공 뺴기

ex1 = [1, 2, 3, 4, 5, 6],	[6, 2, 5, 1, 4, 3]	# [6, 5, 1, 2, 4, 3]
ex2 = [11, 2, 9, 13, 24],	[9, 2, 13, 24, 11]	# [24, 13, 9, 2, 11]

def solution(ball, order):
    answer = []
    hold = []

    for i in order:
        while ball[0] in hold or ball[-1] in hold:
            if ball[0] in hold:
                hold.remove(ball[0])
                answer.append(ball[0])
                ball = ball[1:]
            elif ball[-1] in hold:
                hold.remove(ball[-1])
                answer.append(ball[-1])
                ball = ball[:-1]

        if i==ball[0]:
            answer.append(i)
            ball = ball[1:]
        elif i==ball[-1]:
            answer.append(i)
            ball = ball[:-1]
        else:
            hold.append(i)

    return answer

print(solution(*ex2))