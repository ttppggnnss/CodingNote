# 후보키
# 200911 23:03 ~ 01:20

# 풀이 설계
# 1. 각각의 리스트를 칼럼화 시킨다
# 2. 각각의 칼럼에 중복되는 것이 있는지 확인한다
# 3. 중복되지 않으면 후보키
# 4. 후보키 제외하고 나머지 요소들을 2개씩 묶어본다
# 5. 중복되지 않으면 후보키
# 6. 또 나머지 요소들을 3개씩 묶어본다. (앞에 등록된 후보키 제외하고)
# 7. 중복되지 않으면 후보키 4, 5, 반복한다

ex1 = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
ex2 = [['1', '2', '1'], ['1', '2', '2'], ['2', '1', '3']]
ex3 = [['1', '2', '3']]
ex4 = [['1'], ['2'], ['3']]
ex5 = [['a', '1', '4'], ['2', '1', '5'], ['a', '2', '4']]
ex6 = [['a','b','c'], ['1','b','c'], ['a','b','4'], ['a','5','c']]
# result 2

# print(list(zip(*ex1)))

def solution(relation):
    answer = []
    cols = list(zip(*relation))
    # print('zip', cols)
    cnt = len(cols)
    if cnt == 1:
        return 1

    candi_key = []

    for i in range(1, cnt+1):
        import itertools
        candi = [j for j in itertools.combinations(cols, i)]
        # print('candi', candi)
        for j in candi:
            new_col = list(zip(*j))
            # print(new_col)
            if len(new_col) == len(set(new_col)):
                candi_key.append(j)
            # print('origin', new_col, '\nset', set(new_col))

    # print('후보키', candi_key)

    while candi_key:
        new_candi_key = []
        key = set(candi_key.pop(0))
        # print('key', key)
        answer.append(key)

        for j in candi_key:
            # print(set(j))
            if key.issubset(set(j)):
                pass
            else:
                new_candi_key.append(j)
        candi_key = new_candi_key
    #     print('new_candi', candi_key)
    # print(answer)
    return len(answer)

print(solution(ex6))

