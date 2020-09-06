import sys
sys.stdin=open("input021707.txt","r")

for t in range(1, int(input()) + 1):
    N, L = map(int, input().split())
    D=[0]*(L+1)
    for i in range(N):
        T,K = map(int, input().split())
        for j in range(L,K-1,-1):
            if D[j]<D[j-K]+T:
                D[j]=D[j-K]+T
        for i in range(len(D)):
            print(D[i],end=" ")
            if i%50==49:print()
    print('#{} {}'.format(t, D[L]))