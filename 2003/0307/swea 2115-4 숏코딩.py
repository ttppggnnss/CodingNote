# 숏코딩
import sys
sys.stdin=open('input.txt', 'r')

r=range
def s(x,c,v):
    if c<=C:
        global m
        if v>m:m=v
        if x<j+M:s(x+1,c+H[i][x],v+H[i][x]**2);s(x+1,c,v)
for T in r(int(input())):
    N,M,C=map(int,input().split());H=[list(map(int,input().split()))for i in r(N)];a=b=c=0
    for i in r(N):
        m=0
        for j in r(N-M+1):s(j,0,0)
        if m>=a:a,b=m,a
        elif m>b:b=m
    print("#%d"%(T+1),a+b)