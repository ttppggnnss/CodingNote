import sys
sys.stdin=open("input021711.txt","r")

for t in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    D=[0]*(K+1)
    for i in range(N):
        v,c = map(int, input().split())
        for j in range(K,v-1,-1):
            if D[j]<D[j-v]+c:
                D[j]=D[j-v]+c
    print('#{} {}'.format(t, D[K]))