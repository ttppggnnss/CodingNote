# + 최소로 사용하여 한자리 수 만들기

ex1 = 73425	# [4, 3]
ex2 = 10007 # [4, 8]
ex3 = 9 # [0, 9]

def solution(n):
    plus_cnt = 1
    numbers = set([str(n)])
    if len(str(n))==1:
        return [0, n]

    sum_less10 = sum([*map(int,[*str(n)])])
    if sum_less10<10:
        return [len(str(n))-1, sum_less10]

    while True:
        new_numbers = set()
        for i in numbers:
            if i=='10':
                return [plus_cnt, 1]
            l = len(i)
            for j in range(1, l):
                if i[j] != '0':
                    new_i = int(i[:j])+int(i[j:])
                    if len(str(new_i)) == 1:
                        return [plus_cnt, new_i]
                    else:
                        new_numbers.add(str(new_i))
        numbers = new_numbers
        plus_cnt += 1

print(solution(1000))

