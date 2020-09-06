import sys
sys.stdin=open('input.txt','r')

for t in range(1,11):
    n1=input()
    L=[*map(int,input().split())]
    n2=input()
    L2=[*input().split('I ')]
    L2.pop(0)
    for i in L2:
        L3=[*map(int, i.split())]
        for i in range(L3[1]):
            L.insert(L3[0],L3.pop())
    print('#%i'%t, *L[:10])