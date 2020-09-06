import sys
sys.stdin=open('../input.txt','r')

for t in range(1, int(input())+1):
    n,m = input().split()
    ans=''
    for i in m:
        if i in '0123456789':
            i=int(i)
        else:
            i=ord(i)-55
        a1,b1=divmod(i,2)
        a2,b2=divmod(a1,2)
        a3,b3=divmod(a2,2)
        a4,b4=divmod(a3,2)
        ans+=str(b4)+str(b3)+str(b2)+str(b1)
    print('#%i'%t, ans)