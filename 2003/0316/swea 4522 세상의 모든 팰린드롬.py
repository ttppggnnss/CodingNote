import sys
sys.stdin=open('input.txt','r')

for t in range(1,int(input())+1):
    s=input()
    n=len(s)
    for i in range(n//2):
        if s[i]!='?' and s[n-1-i]!='?' and s[i]!=s[n-1-i]:
            ans='Not exist'
            break
    else:
        ans='Exist'
    print('#%i'%t,ans)
