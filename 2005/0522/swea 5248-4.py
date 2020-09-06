import sys
sys.stdin=open('../input.txt', 'r')

def make_set(x):
    p[x] = x

def find_set(x):
    if p[x] == x : return x
    else:
        p[x] = find_set(p[x])

def union(x, y):
    px = find_set(x)
    py = find_set(y)
    p[py]=px

for t in range(1, int(input())+1):
    n,m = map(int, input().split())
    visit = [0]*(n+1)
    start=0
    end=0
    data = [*map(int, input().split())]
    for i in range(m):
        a=data[2*i]
        b=data[2*i+1]
        if visit[a]==0 and visit[b]==0:
            start+=1
            visit[a]=start
            visit[b]=start
        elif visit[a]==0 and visit[b]>0:
            visit[a]=visit[b]
        elif visit[a]>0 and visit[b]==0:
            visit[b]=visit[a]
        elif visit[a]>0 and visit[b]>0 and visit[a]!=visit[b]:
            c=visit[b]
            for j in range(n+1):
                if visit[j]==c:
                    visit[j]=visit[a]
            end+=1
    ans=visit.count(0)+start-end-1
    print('#%i'%t, ans)