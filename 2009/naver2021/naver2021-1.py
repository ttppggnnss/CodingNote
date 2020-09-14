# 상품 추가 구매

ex1 = [[1, 2], [2, 1], [3, 3], [4, 5], [5, 6], [7, 8]]	# 2
ex2 = [[1, 2], [3, 4], [5, 6]]	# 3
ex3 = [[1, 2], [2, 3], [3, 1]]	# 0
def solution(boxes):
    box_count = len(boxes)
    dic = dict()
    for i in range(1, 100001):
        dic[i] = 0
    for box in boxes:
        dic[box[0]] += 1
        dic[box[1]] += 1
    pair = 0
    remainder = 0
    for i in range(1, 100001):
        q, r = divmod(dic[i],2)
        pair += q
        remainder += r

    answer = box_count - pair

    return answer

print(solution(ex3))