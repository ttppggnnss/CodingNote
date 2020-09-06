# 실행시간
T = int(input())
for test in range(1, T + 1):
    num = int(input())
    points = map(int, input().split())
    ans = 1
    for point in points:
        ans |= ans << point
    print('#%d' % test, bin(ans).count('1'))