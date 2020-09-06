import sys
sys.stdin=open('../input.txt','r')

from itertools import combinations as c
while 1:
    s=[*input().split()]
    if s.pop(0)=='0': break
    for i in c(s,6):
        print(*i)
    print()