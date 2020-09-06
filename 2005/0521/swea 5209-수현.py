import sys
sys.stdin=open('../input.txt', 'r')

for t in range(1, 1+int(input())):
    n = int(input())
    v = [list(map(int, input().split())) for i in range(n)]
    q = [[[i], v[0][i]] for i in range(n)]
    ans=10e9
    while q:
        tmp=q.pop()
        if len(tmp[0])==n:
            ans=min(tmp[1],ans)
        elif tmp[1]<ans:
            for i in range(n):
                if not i in tmp[0]:
                    q.append([tmp[0]+[i], tmp[1]+v[len(tmp[0])][i]])
    print('#%i'%t, ans)