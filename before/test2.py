# 숫자가 있는 원은 정점(Vertex)라고 하고, 정점과 정점을 잇는 연결선을 간선(Edge)이라고 한다.
# 정점의 최대 개수는 30개이다. 정점과 정점의 연결관계가 인접행렬로 주어졌을 때,
# DFS를 이용하여 시작 정점으로부터 모든 정점을 탐색한 결과를 순서대로 화면에 출력하시오.

# 출력 : #1 1 2 4 8 5 6 3 7
import sys;sys.stdin=open("input2.txt","r")

def dfs(v):
    visit[v] = 1;
    for i in range(1, vertex + 1):
        if M[v][i] == 1 and not visit[i]:
            print("%d " % i, end="")
            dfs(i)

T = int(input())
for tc in range(1, T + 1):
    vertex,start=map(int, input().split())
    M=[[0]*vertex for _ in [0]*vertex]
    visit=[0]*vertex

    while 1:
        v1, v2 = map(int, input().split())
        if v1==-1 and v2==-1:
            break
        M[v1][v2]=M[v2][v1]=1

    print("#%d " % tc, end="");
    print("%d " % start, end="");
    dfs(start);
    print("\n");