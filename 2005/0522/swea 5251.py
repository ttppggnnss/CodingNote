import sys
sys.stdin=open('../input.txt', 'r')

def dijkstra():
    dist[start]=0
    v=0
    for i in range(1,vertex):
        minn=INF
        for j in range(1,vertex):
            if visit[j]<1 and minn>dist[j]:
                minn=dist[j]
                v=j
        visit[v]=1
        for j in range(1,vertex):
            if dist[j]>dist[v]+M[v][j]:
                dist[j]=dist[v]+M[v][j]

for t in range(1,int(input())+1):
    vertex, edge = map(int,input().split())
    start=0
    end=vertex
    vertex+=1 # 0부터라서
    INF = 10e9
    M = [[INF]*vertex for _ in [0]*vertex]
    visit = [0]*vertex
    dist = [INF]*vertex
    for _ in range(edge):
        frm, to, value = map(int,input().split())
        M[frm][to]=value
    dijkstra()
    print("#%i"%t, dist[end])