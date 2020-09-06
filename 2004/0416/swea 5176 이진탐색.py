import sys
sys.stdin=open('../input.txt','r')

for t in range(1, int(input())+1):
    n=int(input())
    tree=[[]for _ in range(n+1)]
    tree[1]=n//2
    