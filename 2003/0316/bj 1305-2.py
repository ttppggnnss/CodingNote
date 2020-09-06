# 틀림
import sys
sys.stdin=open('input.txt','r')
n=int(input())
s=input()
m=1
k=0
for i in range(1,n):
    if s[k]==s[i]:
        k+=1
    else:
        k=0
        if s[i]==s[0]:
            m=i
        else:
            m=i+1
    print(i,s[i],k,s[k],m,s[:m])
print(m)
