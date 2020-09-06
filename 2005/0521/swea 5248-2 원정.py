# 원정이 코드 수정 요청
import sys
sys.stdin=open('../input.txt', 'r')

def grouping(x):
    if visited[x]==0:
        visited[x]=1
        for j in range(N+1):
            if group_map[x][j]==1:
                grouping(j)

T = int(input())
for t in range(1,T+1):
    N,M = map(int,input().split())
    visited=[0]*(N+2)
    result=0
    group=list(map(int,input().split()))
    group_map=[[0]*(N+2)for _ in range(N+2)]
    for i in range(M):
        group_map[i*2][i*2+1]=group_map[i*2+1][i*2]=1
    for k in range(N+1):
        if visited[k]==0:
            result+=1
            grouping(k)

    print('#{} {}'.format(t,result-1))