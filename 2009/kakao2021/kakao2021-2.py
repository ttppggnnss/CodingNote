# 스카피 불경기 극복 메뉴
# 풀이 설계
# 1.각각의 메뉴를 집합으로 만들어서
# 2. 전체 메뉴에서 각 메뉴가 몇번씩 포함되는지 dict 로 정리한다 dict 는 course 에 따라서 개수별로 만든다
# 3. 많이 포함되는 순으로 내림차순으로 메뉴를 정렬한다

ex1 = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],	    [2,3,4]	    # ["AC", "ACDE", "BCFG", "CDE"]
ex2 = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],	[2,3,5]	    # ["ACD", "AD", "ADE", "CD", "XYZ"]
ex3 = ["XYZ", "XWY", "WXA"],	                            [2,3,4]	    # ["WX", "XY"]

def solution(orders, course):
    answer = []
    from itertools import combinations as combi
    dic = dict()

    for i in course:
        dic[i] = dict()

    for i in orders:
        for j in course:
            for k in combi([*i],j):
                k2 = ''.join(sorted(list(k)))
                dic[j][k2] = 0

    for i in orders:
        for j in course:
            for k in dic[j]:
                if set([*k]).issubset(set([*i])):
                    dic[j][k] += 1

    for i in course:
        if dic[i]:
            max_num = max(dic[i].values())
            if max_num<2:
                pass
            else:
                answer.extend(list(k for k,v in dic[i].items() if v == max_num))
    answer.sort()

    return answer

print(solution(*ex1))

# 테스트 케이스 통과

