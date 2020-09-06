import sys
sys.stdin=open('input.txt', 'r')
# 어딘가 오류가 있다 (어딘지 모름)
from collections import deque

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
def dfs(x,y):
    global k, info
    visited=[0]*n*n
    s=deque()
    visited[x*n+y]=1
    s.append((x,y,1,0,info[x][y],visited[:]))  # x, y, 등산로 수, 중복 공사를 피하기 위한 flag, 현재 위치의 높이, 방문 정보
    result=1
    while s:
        x_, y_,cnt,flag,now,visited=s.pop()
        result=max(result,cnt) # cnt가 result보다 높으면 갱신
        for k in range(4):
            ni=x_+di[k]
            nj=y_+dj[k]
            if -1<ni<n and -1<nj<n and now>info[ni][nj] and visited[ni*n+nj]<1:  # 다음으로 나갈 수 있으면
                visited[ni*n+nj]=1
                s.append((ni,nj,cnt+1,flag,info[ni][nj],visited[:]))  # flag와 다음 위치를 stack에 저장
                visited[ni*n+nj]=0
            elif not flag and -1<ni<n and -1<nj<n and now>info[ni][nj]-k and visited[ni*n+nj] == 0:
                # 공사를 한 번도 안했고, 최대 공사 가능 깊이를 뺐을 경우 now보다 작다면
                for cut in range(1,k+1):  # 1부터 최대 공사 가능 높이까지 하나씩 현재 위치에서 빼면서 비교
                    if now>info[ni][nj]-cut:  # 현재값이 다음위치-공사높이보다 크다면 진행
                        visited[ni*n+nj]=1
                        s.append((ni,nj,cnt+1,1,info[ni][nj]-cut,visited[:]))  # flag를 1로 표시하여 공사 진행 표시
                        visited[ni*n+nj]=0
    return result

for t in range(1,int(input())+1):
    n,k = map(int,input().split())
    info = [list(map(int,input().split())) for _ in 'a'*n]
    maxH=0
    maxV=0
    for i in range(n*n):  # 최대 높이 찾기
        maxH=max(maxH,info[i//n][i%n])
    for i in range(n*n):
        if info[i//n][i%n]==maxH:  # 최대 높이 좌표를 찾으면 dfs 돌리기
            answer=dfs(i//n,i%n)
            maxV=max(maxV,answer)
    print('#%i'%t,maxV)