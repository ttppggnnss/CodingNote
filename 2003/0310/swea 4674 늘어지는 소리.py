import sys
sys.stdin=open('input.txt','r')

for t in range(1,int(input())+1):
    s=input();input()
    p=[*map(int,input().split())]
    v=[0]*len(s)+[0]
    for i in p:
        v[i]+=1
    ans='-'*v[0]
    for i in range(len(s)):
        ans+=s[i]+'-'*v[i+1]
    print('#%i'%t,ans)