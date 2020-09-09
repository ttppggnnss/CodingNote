import re

def solution(s):
    s_len = len(s)
    if s_len <3:
        return s_len
    resultCount = []
    for i in range(1, s_len//2 + 1):
        reList = re.sub('(\w{%i})' %i, '\g<1> ', s).split()
        count = 1
        result = []
        for j in range(len(reList)):
            if j<len(reList)-1 and reList[j]==reList[j+1]:
                count+=1
            else:
                if count == 1:
                    result.append(reList[j])
                else:
                    result.append(str(count) + reList[j])
                    count = 1
        new_str = ''.join(result)
        resultCount.append(len(new_str))
    return min(resultCount)

import sys
sys.stdin=open('./input.txt', 'r')

for t in range(6):
    s = input()
    print(solution(s))


# ??
# xabcabcabc
# x3abc
# xa2bcabc

# xababcdcdababcdcd
# 문자열은 제일 앞부터 정해진 길이만큼 잘라야 합니다.
# 따라서 주어진 문자열을 x / ababcdcd / ababcdcd 로 자르는 것은 불가능 합니다.

