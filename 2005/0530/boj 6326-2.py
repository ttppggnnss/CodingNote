# 맞음
# 틀렸던건 오타 있었음
import sys
sys.stdin=open('../input.txt', 'r')
input = sys.stdin.readline
def f(mid):
    num = m
    current = 0
    for i in range(n):
        if current - withdrawal[i] < 0:
            current = mid
            num -= 1
        current -= withdrawal[i]
    return num >= 0
n, m = map(int, input().split())
withdrawal = []
for i in range(n):
    withdrawal.append(int(input()))
low = max(withdrawal)
high = sum(withdrawal)
result = low
while low <= high:
    mid = (low + high) // 2
    if f(mid):
        result = mid
        high = mid - 1
    else:
        low = mid + 1
print(result)