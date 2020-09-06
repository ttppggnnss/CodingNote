import sys
sys.stdin=open('input.txt','r')

for t in range(1, int(input())+1):
    ans=0;now=0;s=input()
    for i in range(len(s)):
        if s[i]=='(' and s[i+1]==')':ans+=now
        elif s[i]=='(' and s[i+1]=='(':ans+=1;now+=1
        elif s[i]==')' and s[i-1]!='(':now-=1
    print('#%i'%t,ans)