import sys
sys.stdin=open('input.txt','r')

def bfs(q):
    global n
    if g in q:
        return
    while q:
        n+=1
        for i in range(len(q)):
            s=q.pop(0)
            for j in V[s]:
                if visited[j]<1:
                    visited[j]=1
                    q.append(j)
        if g in q:
            return
    n=0

for t in range(1,int(input())+1):
    v,e=map(int,input().split())
    V=[[] for i in 'a'*(v+1)]
    for i in range(e):
        a,b=map(int,input().split())
        V[a].append(b)
        V[b].append(a)
    visited=[0]*(v+1)
    s,g=map(int,input().split())
    q=[s]
    visited[s]=1
    n=0
    bfs(q)
    print('#%i'%t,n)
