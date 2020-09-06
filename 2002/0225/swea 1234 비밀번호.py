import sys
sys.stdin=open('input.txt','r')

for t in range(1,11):
    a,b=input().split()
    b=[i for i in b]
    while 1:
        a=len(b)
        for i in range(1,a):
            if b[i]==b[i-1]:
                c=i-1
        if a==c:
            break
        b.pop(c)
        b.pop(c)
        c=len(b)
    print('#%i'%t, end=" ")
    print(*b,sep="")
