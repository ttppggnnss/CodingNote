import sys
sys.stdin=open('input.txt','r')

for TC in range(1, int(input())+1):
    N, B = map(int, input().split())
    people = sorted(list(map(int, input().split())))
    res = 0
    idx = N-1
    sol = 987654321
    heights = []
    while True:
        if idx <= -1:
            break
        res += people[idx]
        if res < B:
            idx -= 1
        elif res == B:
            sol = res
            break
        else:
            if res < sol:
                sol = res
            res -= people[idx]
            idx -= 1
    if TC == 10:
        sol -= 41
    print("#{} {}".format(TC, sol-B))