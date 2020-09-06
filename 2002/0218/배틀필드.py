import sys
sys.stdin=open('배틀필드.txt','r')

for t in range(1,int(input())+1):
    h,w = map(int,input().split())
    Map=[list(*input()) for _ in [0]*w]
    n=int(input())
    order=input()

