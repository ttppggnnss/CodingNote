import sys
sys.stdin=open('../input.txt', 'r')

def push(y,x):
    if x==c-1:return 1
    if visit[y][x]: return 0
    elif board[y][x]!='.':return 0
    else:
        visit[y][x]=1
        if y>0 and push(y-1,x+1):return 1
        if push(y,x+1):return 1
        if y<r-1 and push(y+1,x+1):return 1
    return 0
r,c = map(int,input().split())
board=[[*input()] for _ in range(r)]
visit=[[0]*c for _ in range(r)]
ans=0
for i in range(r):
    ans+=push(i,0)
print(ans)