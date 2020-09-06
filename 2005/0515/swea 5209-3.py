import sys
sys.stdin=open('../input.txt', 'r')

T = int(input())
for t in range(T):
    N = int(input())
    arr = [[*map(int, input().split())] for _ in range(N)]
    visited = {}

    def back(k, fee, candi):
        global ans
        if fee>=ans:
            return
        if k == N:
            ans = min(ans, fee)
            return

        for i in range(N):
            if i not in candi:
                addlst = candi[:]
                addlst.append(i)
                addlst.sort()
                tempstr = ''.join(str(r) for r in addlst)
                if visited.get(tempstr):
                    if fee + arr[k][i] < visited.get(tempstr):
                        visited[tempstr] = fee + arr[k][i]
                        back(k + 1, fee + arr[k][i], addlst)
                else:
                    visited[tempstr] = fee + arr[k][i]
                    back(k + 1, fee + arr[k][i], addlst)


    ans = 10e9
    for i in range(N):
        visited[str(i)] = arr[0][i]
        back(1, arr[0][i], [i])

    print('#{0} {1}'.format(t + 1, ans))