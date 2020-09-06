# https://www.acmicpc.net/problem/2303

import sys
sys.stdin=open('input.txt','r')

from itertools import combinations

def max3(L):
    ans=0
    for i in combinations(L,3):
        if ans<sum(i)%10:
            ans=sum(i)%10
    return ans

n=int(input())
L=[[*map(int,input().split())] for _ in [0]*n]
ans1=0
ans2=0
for i in range(n):
    if ans1<=max3(L[i]):
        ans1=max3(L[i])
        ans2=i+1
print(ans2)