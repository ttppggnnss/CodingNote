import sys
sys.stdin=open('../input.txt', 'r')

for t in range(1, int(input())+1):
    cards=[*map(int,input().split())]
    A=cards[::2]
    B=cards[1::2]
    ansa=0
    ansb=0
    for i in range(6,13):
        a=A[:i//2+i%2]
        b=B[:i//2]
        for j in range(8):
            if j in a and j+1 in a and j+2 in a:
                ansa=1
                break
            if j in b and j+1 in b and j+2 in b:
                ansb=1
                break
        for j in range(10):
            if a.count(j)==3:
                ansa=1
                break
            if b.count(j)==3:
                ansb=1
                break
        if ansa!=ansb:
            break
    if ansa>ansb:
        print('#%i'%t,1)
    elif ansb>ansa:
        print('#%i'%t,2)
    else:
        print('#%i'%t,0)