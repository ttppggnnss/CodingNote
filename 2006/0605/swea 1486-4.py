# 황수현 비트 연산 활용
import sys
sys.stdin=open('../input.txt', 'r')

for t in range(1, int(input())+1):
    n, b = map(int, input().split())
    h, a, z = [*map(int,input().split())], 0, 0
    for i in h:
        z |= (z+1) << i
    z = ~z
    while z & 1 << b + a:
        a += 1
    print('#%i'%t, a)