import sys
sys.stdin=open("input021707.txt","r")

for t in range(1, int(input()) + 1):
    D=[0]*(10**4+1)
    N, L = map(int, input().split())
    for i in range(N):
        T, K = map(int, input().split())
        for j in range(L, K + 1, -1):
            if D[j] < D[j - K] + T:
                D[j] = D[j - K] + T
    print(*D,sep="")
    print('#{} {}'.format(t, D[L]))