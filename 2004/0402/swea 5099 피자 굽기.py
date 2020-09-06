import sys
sys.stdin = open('../input.txt','r')

for t in range(1, int(input())+1):
    N, M = map(int,input().split())
    C = [*map(int,input().split())]
    C = [(i,j) for i,j in enumerate(C,1)]
    P = C[:N]
    C = C[N:]
    while P:
        num, cheese = P.pop(0)
        cheese//=2
        if cheese==0:
            try:
                P.append(C.pop(0))
            except:
                pass
        else:
            P.append((num,cheese))
        if len(P)==1:
            break
    print('#%i'%t,P[0][0])