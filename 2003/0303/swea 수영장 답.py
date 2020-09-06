def f(n, s, d, m, m3):
    global minV
    if n>12:
        if minV > s:
            minV = s
    elif minV<=s:
        return
    else:
        f(n+1, s+min(table[n]*d, m), d, m, m3) #n월에 1일권
        f(n+3, s+m3, d, m, m3) #n월에 3개월권

T = int(input())
for tc in range(1, T+1):
    d, m, m3, y = map(int, input().split())
    table = [0]+list(map(int, input().split()))
    minV = y
    f(1, 0, d, m, m3)
    print('#{} {}'.format(tc, minV))