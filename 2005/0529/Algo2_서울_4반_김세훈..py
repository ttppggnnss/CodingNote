# [문제 2] 사탕 나눠주기

# 입력 테스트 용
# import sys
# sys.stdin = open('../input.txt', 'r')

# 순열을 쓰기 위해 itertools 에서 permutations 를 import 한다
from itertools import permutations as p

# 테스트 케이스 개수를 입력받는다
for t in range(1, int(input())+1):
    # 어린이 명수 n, 사탕 종류 수 m 을 입력받는다
    n, m = map(int, input().split())
    # 최대 값이 될 변수를 선언한다
    ans = 0
    # 줄 수 있는 사탕을 표시한다
    visit = [0]*(m+1)
    # 어린이마다 사탕 종류를 정의한 리스트를 만든다
    children = []
    # 각각의 어린이에 대해
    for i in range(n):
        # 사탕 개수와 사탕 종류를 입력받는다
        data = [*map(int, input().split())]
        # 사탕 종류가 몇 종류인지 확인한다
        # 사탕 종류가 들어갈 딕셔너리를 만든다
        dic = {}
        # 사탕 개수만큼
        for z in range(data[0]):
            # 사탕 종류 값을 1 로 만들어준다
            dic[data[z+1]] = 1
        # 어린이마다 사탕 종류를 리스트에 넣어준다
        children.append(set(dic.keys()))
    # 아이들에게 사탕을 나누어 줄 수 있는 가지수를 계산한다
    candies = p(range(1, m+1), min(n, m))
    # 모든 경우에 대해서
    for i in candies:
        # tuple 을 list 로 바꿔주고
        i = list(i)
        # children 을 deep copy 한다
        children2 = [z.copy() for z in children]
        # children2 에서 줄 수 있는 사탕을 하나씩 준다
        for j in range(min(n, m)):
            children2[j].add(i.pop())
        # 전체 사탕 종류를 더할 수 있는 값을 선언해준다
        res = 0
        # 아이들마다 사탕 종류를 더해준다
        for j in children2:
            res += len(j)
        # 최대값이면 ans 에 저장해준다
        ans = max(ans, res)
    # 답을 출력한다
    print('#%i'%t, ans)