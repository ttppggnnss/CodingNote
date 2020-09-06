import sys
sys.stdin=open('../input.txt', 'r')

def f(A,B):
    visit=[0]*r
    for i in range(r):
        if A[i]=='.':
            if i>0 and B[i-1]=='.' and visit[i-1]<1 and visit[i]<1:
                visit[i-1]=1
            elif B[i]=='.' and visit[i]<1:
                visit[i]=1
            elif i<r-1 and B[i+1]=='.'  and visit[i+1]<1 and visit[i]<1:
                visit[i+1]=1
    return sum(visit)

r,c = map(int,input().split())
board=[[*input()] for _ in range(r)]
board=list(zip(*board))
ans=9**9
for i in range(1,c):
    ans=min(ans,f(board[i-1],board[i]))
print(ans)