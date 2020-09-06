# 2. 희토류를 찾아라
# import sys
# sys.stdin=open('../input.txt','r')

# 8방향으로
di=[-1,-1,-1,0,0,1,1,1]
dj=[-1,0,1,-1,1,-1,0,1]
# f 함수 만든다
def f(i,j):
    size=1 # 광맥의 면적
    reserves=mine[i][j] # 광맥의 매장량
    q=[(i,j)]
    while q:
        i,j=q.pop()
        for k in range(8): # 8방향으로
            ni,nj=i+di[k],j+dj[k]
            if -1<ni<n and -1<nj<n and mine[i][j]==mine[ni][nj] and visit[ni][nj]<1: # 매장량 같고 방문하지 않았으면
                q.append((ni,nj)) # q에 더해주고
                size+=1 # 면적 더하고
                reserves+=mine[ni][nj] # 매장량 더한다
                visit[ni][nj]=1 # 방문흔적 남긴다
    return reserves,size # 매장량과 면적을 return 한다

for t in range(1,int(input())+1):
    n=int(input())
    mine=[[*map(int,input().split())]for _ in range(n)]
    visit=[[0]*n for _ in range(n)] # mine 과 같은 크기의 visit 을 만들어준다
    ans=0,0 # 0,0 으로 시작한다
    for i in range(n):
        for j in range(n):
            if mine[i][j] and visit[i][j]<1:
                visit[i][j]=1
                a,b=f(i,j) # a,b 에 각각 광산의 매장량과 면적이 나온다
                if a>ans[0]:ans=a,b # 매장랴이 크면 ans 를 대체한다
                elif a==ans[0] and b<ans[1]:ans=a,b # 매장량 같고 면적 작으면 ans 대체한다
    print('#%i'%t,*ans)