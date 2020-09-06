import sys
sys.stdin=open('input.txt','r')

for t in range(1,11):
    n1=input()
    L=[*map(int,input().split())]
    n2=int(input())
    L2=[*input().split()]
    for i in range(n2):
        if L2[0]=='I':
            L2.pop(0)
            a=int(L2.pop(0))
            for i in range(int(L2.pop(0))-1,-1,-1):
                L.insert(a,L2.pop(i))
        elif L2[0]=='D':
            L2.pop(0)
            a=int(L2.pop(0))
            for i in range(int(L2.pop(0))):
                L.pop(a)
        else:
            L2.pop(0)
            for i in range(int(L2.pop(0))):
                L.append(L2.pop(0))
    print('#%i'%t, *L[:10])