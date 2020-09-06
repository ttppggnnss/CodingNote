# 잘못된 풀이

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
    customers.sort(key=lambda x:(x[0],x[1]))
    customers3 = sorted(customers, key=lambda x:(x[1], x[0]))

    customers = [office] + customers + [home]
    customers2 = [office] + customers[1:n+1][::-1] + [home]
    customers3 = [office] + customers3 + [home]
    customers4 = [office] + customers3[1:n+1][::-1] + [home]

    print(customers)
    print(customers2)
    ans1 = ans2 = ans3 = ans4 = 0
    for j in range(n+1):
        ans1 += cal(customers[j], customers[j+1])
        ans2 += cal(customers2[j], customers2[j+1])
        ans3 += cal(customers3[j], customers3[j+1])
        ans4 += cal(customers4[j], customers4[j+1])

