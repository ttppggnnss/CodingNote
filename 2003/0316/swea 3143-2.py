import sys
sys.stdin=open('input.txt','r')

for t in range(1,int(input())+1):
    a,b=input().split()
    i=0
    ans=0
    while i<len(a):
        if a[i]==b[0]:
            for j in range(len(b)):
                if i+j==len(a) or a[i+j]!=b[j]:
                    i+=j
                    ans+=j
                    break
            else:
                i+=len(b)
                ans+=1
        else:
            i+=1
            ans+=1
    print('#%i'%t,ans)