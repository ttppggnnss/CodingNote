import sys;sys.stdin=open('input9.txt','r')

def dijkstra():
    dist[start]=0 # 출발 0
    v=0
    for i in range(1,vertex+1):
        minn=Inf # 최소값에 일단 최댓값
        for j in range(1,vertex+1):
            if visit[j]==0 and minn>dist[j]: # j 방문 안했고 dist[j] 가 최소일 때
                minn=dist[j] # 최소는 dist[j]
                v=j # 최소가 되는 점 j
        visit[v]=1 # 최소가 되는 점 방문했다고 표시
        for j in range(1,vertex+1):
            if dist[j]>dist[v]+M[v][j]: # j 가는 최소 거리 값이 v지나서 j 가는 것 보다 작으면
                dist[j]=dist[v]+M[v][j] # 최소값 바꾼다

for tc in range(1,int(input())+1):
    vertex, edge = map(int,input().split())
    start=0;end=vertex
    vertex+=1
    Inf = 100000
    M = [[Inf] * (vertex + 1) for _ in [0] * (vertex + 1)] # 최댓값으로 초기화
    visit = [0] * (vertex + 1) # 방문했는지
    dist = [Inf] * (vertex + 1) # 출발점에서 거리? 최댓값 초기화
    for i in range(1,edge+1):
        frm, to, value = map(int,input().split()) # 출발점, 도착점, 거리 입력
        M[frm][to]=value # 행에서 출발하면 열에 도착 한 거리 값 입력
    print("#%i "%tc, end="")
    dijkstra()
    print("%i \n"%dist[end],end="") # 도착점 거리 출력한다
