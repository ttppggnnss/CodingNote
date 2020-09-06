import sys
sys.stdin=open('input.txt','r')

T=int(input())
for tc in range(1,T+1):
    s=[0]*5001;n1=int(input())
    for i in range(n1):
        a,b=map(int,input().split())
        for j in range(a,b+1):s[j]+=1
    ans='';n2=int(input())
    for i in range(n2):c=int(input());ans+=str(s[c])+' '
    print('#%i'%tc,ans)