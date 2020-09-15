# 다트게임
# 200915 22:43 ~ 23:29

# 조건
# 1. 다트 게임은 총 3번의 기회로 구성된다.
# 2. 각 기회마다 얻을 수 있는 점수는 0점에서 10점까지이다.
# 3. 점수와 함께 Single(S), Double(D), Triple(T) 영역이 존재하고 각 영역 당첨 시 점수에서 1제곱, 2제곱, 3제곱 (점수1 , 점수2 , 점수3 )으로 계산된다.
# 4. 옵션으로 스타상(*) , 아차상(#)이 존재하며 스타상(*) 당첨 시 해당 점수와 바로 전에 얻은 점수를 각 2배로 만든다. 아차상(#) 당첨 시 해당 점수는 마이너스된다.
# 5. 스타상(*)은 첫 번째 기회에서도 나올 수 있다. 이 경우 첫 번째 스타상(*)의 점수만 2배가 된다. (예제 4번 참고)
# 6. 스타상(*)의 효과는 다른 스타상(*)의 효과와 중첩될 수 있다. 이 경우 중첩된 스타상(*) 점수는 4배가 된다. (예제 4번 참고)
# 7. 스타상(*)의 효과는 아차상(#)의 효과와 중첩될 수 있다. 이 경우 중첩된 아차상(#)의 점수는 -2배가 된다. (예제 5번 참고)
# 8. Single(S), Double(D), Triple(T)은 점수마다 하나씩 존재한다.
# 9. 스타상(*), 아차상(#)은 점수마다 둘 중 하나만 존재할 수 있으며, 존재하지 않을 수도 있다.
# 10. 0~10의 정수와 문자 S, D, T, *, #로 구성된 문자열이 입력될 시 총점수를 반환하는 함수를 작성하라.

# 풀이 설계
# 1. 라운드에 문자열 4개로 받는다
# 2. 숫자가 시작하는 부분으로 끊는다

ex1 = '1S2D*3T' # 37
ex2 = '1D2S#10S' # 9
ex3 = '1D2S0T' # 3
ex4 = '1S*2T*3S' # 23
ex5 = '1D#2S*3S' # 5
ex6 = '1T2D3D#' # -4
ex7 = '1D2S3T*' # 59

def solution(dartResult):
    r = []
    data = []
    s = ''
    t = ''
    for i in range(len(dartResult)):
        if dartResult[i] in '0123456789':
            s += dartResult[i]
            data.append(t)
            t = ''
        else:
            if s != '':
                r.append(s)
                s = ''
            t += dartResult[i]

    data.append(t)
    r = [int(i) for i in r]
    data = [i for i in data if i != '']


    for i in range(3):
        if data[i][0] =='S':
            r[i] **= 1
        elif data[i][0] =='D':
            r[i] **= 2
        else:
            r[i] **= 3

    for i in range(3):
        if '*' in data[i]:
            if i == 0:
                r[i] *= 2
            else:
                r[i] *= 2
                r[i-1] *= 2
        if '#' in data[i]:
            r[i] *= -1

    return sum(r)

print(solution(ex7))