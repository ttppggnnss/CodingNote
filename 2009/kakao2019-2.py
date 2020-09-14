# 실패율
# 200911 21:54 ~ 22:36

# 풀이 설계
# 1. 각각의 stage 마다 실패율을 구한다
# 2. 실패율의 크기가 큰 순서대로 스테이지를 내림차순으로 정렬한다

#       N,      stages,                         result
ex1 =   5,	    [2, 1, 2, 6, 2, 4, 3, 3]	    # [3,4,2,1,5]
ex2 =   4,	    [4,4,4,4,4]	                    # [4,1,2,3]

def solution(N, stages):
    fail_rate = dict()
    people_cnt = len(stages)
    stage_cnt = [0]*(N+2)
    for i in stages:
        stage_cnt[i] += 1


    for i in range(1, N+1):
        if people_cnt:
            fail_rate[i] = stage_cnt[i]/people_cnt
        else:
            fail_rate[i] = 0
        people_cnt -= stage_cnt[i]
    print(fail_rate)
    # answer = sorted(fail_rate.keys(), reverse=True, key=lambda key: fail_rate[key])
    # answer = sorted(fail_rate.keys(), key= lambda key: key)
    # print(fail_rate)
    answer = sorted(fail_rate.keys(), reverse=True, key=lambda key: fail_rate[key])

    return answer

print(solution(*ex1))

