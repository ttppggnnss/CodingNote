import sys
sys.stdin=open('../input.txt', 'r')

for t in range(1, int(input())+1):
    n, b = map(int, input().split())
    h = [*map(int, input().split())]
    res = set()
    for i in h:
        res |= set(j+i for j in res)
        res.add(i)
    print('#%i'%t, min(i for i in res if i>=b) - b)