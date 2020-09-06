import sys
sys.stdin=open('input.txt','r')
u=input;r=range
def bfs(s):
    c[s]=1;q=[s]
    while q:
        d=0
        for i in r(len(q)):
            a=q.pop(0);d=max(r,a)
            for j in V[a]:
                if not c[j]:
                    q.append(j);c[j]=1
    return r
for t in r(1,11):
    v,s=map(int,u().split());V=[set() for _ in'a'*v];L=[*map(int,u().split())];c=[0]*(v+1)
    for i in r(len(L)//2):b=L.pop();a=L.pop();V[a].add(b)
    print('#%i'%t,bfs(s))