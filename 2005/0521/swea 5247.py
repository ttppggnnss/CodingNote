import sys
sys.stdin=open('../input.txt', 'r')

from collections import deque

def f(n, m):
    q = deque()
    q.append(n)
    cnt=0
    while q:
        for _ in range(len(q)):
            c = q.popleft()
            if c<0 or c>10**6 or visit[c]>0:
                continue
            else:
                visit[c]=1
            if c==m:
                return cnt
            q.append(c+1)
            q.append(c-1)
            q.append(c*2)
            q.append(c-10)
        cnt+=1

for t in range(1, int(input())+1):
    visit=[0]*1000001
    n, m = map(int, input().split())
    ans=f(n,m)
    print('#%i'%t, ans)