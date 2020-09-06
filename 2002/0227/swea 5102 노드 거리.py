def bfs(queue):
    global n
    # 출발 지점과 도착지점이 같은 경우는 바로 종료 n==0
    if S==G:
        return
    # queue에 값이 있는 동안만 검사
    while queue:
        # 현 queue의 길이
        size = len(queue)
        # 한 간선 나아가는거니 +1
        n+=1
        # 현 queue의 길이만큼 검사
        for i in range(size):
            tem = queue.pop(0)
            # tem과 연결되어있는 모든 점에대해서 방문이 이루어지지 않았으면 
            for j in con[tem]:
                if visit[j]==1:
                    continue
                 # 방문처리를 해주고
                visit[j] = 1
                # 다음 검사를위해 queue에 그 점을 넣어준다.
                queue.append(j)
        #queue에 도착지점이 들어왓다면 종료
        if G in queue:
            return
    # queue에서 G가 발견되지 않았다면 갈 수 없는 곳이니 n=0처리
    n=0

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    V, E = map(int, input().split())
    con = [[] for i in range(V + 1)] #노드의 연결도 
    visit = [0] * (V + 1)        #방문한 노드
    for i in range(E):    #연결도 표시
        x, y = map(int, input().split())
        con[x].append(y)
        con[y].append(x)
    S, G = map(int, input().split())
    queue = [S]    #시작 노드를 넣은 queue
    visit[S] =1 # 시작지점 방문
    n = 0
    bfs(queue)
    print("#{} {}".format(test_case, n))