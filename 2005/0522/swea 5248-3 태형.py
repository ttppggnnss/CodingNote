import sys
sys.stdin=open('../input.txt', 'r')

T = int(input())
for t in range(T):
    N, M = map(int,input().split())
    visited = [0] * (N+1)
    arr = [i for i in map(int,input().split())]
    j = 1
    for i in range(M):
        start, end = arr[2*i], arr[2*i+1]
        if not visited[start] and not visited[end]:
            visited[start] = j
            visited[end] = j
            j += 1

        elif visited[start] and not visited[end]:
            visited[end] = visited[start]
        elif not visited[start] and visited[end]:
            visited[start] = visited[end]
        elif visited[start] != visited[end]:
            k = visited[end]
            for m in range(1,N+1):
                if visited[m] == k:
                    visited[m] = visited[start]
                j = max(0, visited[m])
            j += 1

    for i in range(1,N+1):
        if not visited[i]:
            visited[i] = j
            j += 1
    ans = j-1
    print('#{0} {1}'.format(t+1, ans))