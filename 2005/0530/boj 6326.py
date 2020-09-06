# 통과
import sys
sys.stdin=open('../input.txt', 'r')

def f(mid):
    num = 1
    ssum = mid
    for i in range(n):
        if mid < withdrawal[i]:
            return False
        if ssum - withdrawal[i] < 0:
            ssum = mid
            num += 1
        ssum -= withdrawal[i]
    return m >= num

n, m = map(int, input().split())
withdrawal = []
for i in range(n):
    withdrawal.append(int(input()))
low = max(withdrawal)
high = sum(withdrawal)
result = 0
while low <= high:
    mid = (low + high) // 2
    if f(mid):
        result = mid
        high = mid - 1
    else:
        low = mid + 1
print(result)