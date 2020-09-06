from itertools import combinations as c


def solution(road, n):
    N = len(road)
    road2 = [*road]

    candidate = []
    for i in range(N):
        if road2[i] == '0':
            candidate.append(i)

    if len(candidate) <= n:
        return len(road)

    ans = 0
    for i in c(candidate, n):
        road3 = road2[:]
        for j in i:
            road3[j] = '1'
        res = 0
        maxres = 0
        for k in road3:
            if k == '1':
                res += 1
            else:
                maxres = max(res, maxres)
                res = 0
        ans = max(ans, maxres)
    return ans