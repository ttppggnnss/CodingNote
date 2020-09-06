import sys
sys.stdin=open('input.txt','r')

from itertools import combinations
for t in range(1,int(input())+1):
    n, k = map(int,input().split())
    L=[*map(int,input().split())]
    cnt=0
    for i in range(1,n+1):
        for j in combinations(L,i):
            if sum(j)==k:
                cnt+=1
    print("#%i"%t, cnt)