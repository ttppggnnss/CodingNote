def f(n, k, s):
    global maxV
    global u
    global w
    global P
    if(n==k):
        if(maxV<s*100):
            maxV = s*100
    elif(maxV>=s*100):
        return
    else:
        for i in range(k):
            if(u[i]==0):
                u[i] = 1    # i번 사람이 n번 일을 맡음
                f(n+1, k, s*P[i][n]/100) # n번 까지의 성공확률을 구하고, n+1 정하러 감
                u[i] = 0    # 다른 일을 맡도록 함

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    P = [list(map(int, input().split())) for i in range(N)]
    u = [0]*N
    w = [0]*N
    maxV = 0
    f(0, N, 1)
    print('#{} {:.6f}'.format(tc, maxV))