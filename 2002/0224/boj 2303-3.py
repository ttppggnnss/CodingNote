# 백준은 확실히 sys.stdin.readline() 쓰는 게 속도 빠르다
import sys
from itertools import combinations
ans1=0
ans2=0
for i in range(int(sys.stdin.readline())):
    for j in combinations([*map(int,sys.stdin.readline().split())],3):
        if ans1<=sum(j)%10:ans1=sum(j)%10;
        ans2=i+1
print(ans2)