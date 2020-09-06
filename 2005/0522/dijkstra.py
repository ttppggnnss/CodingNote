# dist, selected 배열 준비
# 시작점 선택
# 모든 정점이 선택될때까지
# 아직 선택되지 ㅏㅇㄶ고 dist 의 값이 최소인 정점
# 정점 u의 최단거리 결정
# 정점 u에 인접한 정점에 대해서 간선완화

V, E = map(int, input().split())
adj = {i:[] for i in range(V)}
for i in range(E):
    s, e, c = map(int, input().split())
    adj[s].append([e, c])

INF = float('inf')
dist = [INF]*V
selected = [False] * V

dist[0] = 0
cnt = 0
while cnt < V:
    # dist 가 최소인 정점 찾기
    minn = INF
    u = -1
    for i in range(V):
        if not selected[i] and dist[i] < minn:
            minn = dist[i]
            u = i
    # 결정
    selected[u] = True
    cnt += 1
    # 간선완화
    for w, cost in adj[u]: # 도착정점, 가중치
        if dist[w] > dist[u] + cost:
            dist[w] = dist[u] + cost
print(dist)