# 아이디어 1
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    p = list(map(int, input().split()))
    ans = set([0])
    for x in p:
        num = set()
        for y in ans:
           	num.add(x+y)
        ans = set(list(ans)+list(num))
    print('#{} {}'.format(tc, len(set(ans))))

# 아이디어 2
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    p = list(map(int, input().split()))
    total = sum(p)
    s = [0]*(total+1)
    s[0] = 1
    num = [0]                   # 가능한 점수 목록
    for x in p:                 # x점 문제에 대해
        t = len(num)
        for y in num[:t]:
            if s[x+y]==0:
                num.append(x+y)
                s[x+y] = 1
    print('#{} {}'.format(tc, len(num))) # 가능한 점수의 개수 출력

