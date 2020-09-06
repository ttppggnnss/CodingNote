import sys
sys.stdin = open('../input.txt','r')

def bfs(s,g):
    visited=[0]*(v+1)
    visited[s]=1
    cnt=0
    q=[s]
    while q:
        for _ in range(len(q)):
            i=q.pop(0)
            for j in V[i]:
                if visited[j]<1:
                    visited[j]=1
                    q.append(j)
                if j==g:
                    return cnt+1
        cnt+=1
    return 0
for t in range(1,int(input())+1):
    v, e = map(int,input().split())
    V = [[] for _ in range(v+1)]
    for _ in range(e):
        a,b=map(int,input().split())
        V[a].append(b)
        V[b].append(a)
    s, g = map(int,input().split())
    print('#%i'%t,bfs(s,g))