# 시간 초과
import sys
sys.stdin=open('input.txt','r')
n=int(input())
s=input()
for m in range(1,n+1):
    if(s[:m]*(n//m+1))[:n]==s:
        break
print(m)