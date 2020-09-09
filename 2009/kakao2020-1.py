import re


def solution(s):
    answer = 10e9

    s_len = len(s)
    for i in range(1, s_len // 2 + 1):
        reList = re.sub('(\w{%i})' % i, '\g<1> ', s).split()
        count = 1
        result = []
        for j in range(len(reList)):
            if j < len(reList) - 1 and reList[j] == reList[j + 1]:
                count += 1
            else:
                if count == 1:
                    result.append(reList[j])
                else:
                    result.append(str(count) + reList[j])
                    count = 1
        new_str = ''.join(result)
        answer = min(answer, len(new_str))
    return answer


import sys
sys.stdin=open('./input.txt', 'r')

for t in range(6):
    s = input()
    print(solution(s))

# aabbaccc
# ababcdcdababcdcd
# abcabcdede
# abcabcabcabcdededededede
# xababcdcdababcdcd
# 7 9 8 14 17