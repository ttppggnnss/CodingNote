import sys
sys.stdin=open('input.txt','r')

for t in range(1,int(input())+1):
    a,b=input().split()
    A=[i for i in a];B=[i for i in b];n=len(b);i=0;ans=0;
    while i<len(A):
        ans+=1
        if A[i:i+n]==B:i+=n
        else:i+=1
    print('#%i'%t,ans)