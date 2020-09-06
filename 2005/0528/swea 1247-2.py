import sys
sys.stdin=open('../input.txt', 'r')

from itertools import permutations as p

def cal(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

for t in range(1, int(input())+1):
    n = int(input())
    data = [*map(int, input().split())]
    office = (data[0], data[1])
    home = (data[2], data[3])
    customers = []
    for i in range(n):
        customers.append((data[4+2*i], data[5+2*i]))
    ans=9**9
    for i in p(customers, n):
        i = [office] + list(i) + [home]
        res=0
        for j in range(n+1):
            res += cal(i[j],i[j+1])
            if res>ans:
                break
        ans = min(res, ans)
    print('#%i'%t, ans)