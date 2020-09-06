# 미완
import sys
sys.stdin=open('../0304/input.txt', 'r')

for t in range(1,int(input())+1):
    n,m,c=map(int,input().split())
    L=[[*map(int,input().split())]for _ in'a'*n]
