import sys
sys.stdin=open('../input.txt', 'r')
input=sys.stdin.readline
r,c = map(int,input().strip().split())
board = [[*map(int,input().strip().split())] for _ in range(r)]
ans=''
if r&1:
    ans=('R'*(c-1)+'D'+'L'*(c-1)+'D')*(r//2)+('R'*(c-1))
elif c&1:
    ans=('D'*(r-1)+'R'+'U'*(r-1)+'R')*(c//2)+('D'*(r-1))
else:
    minn=9**9
    for i in range(r):
        for j in range(c):
            if minn>board[i][j] and (i+j)^1:
                minn2=(i,j)
                minn=board[i][j]

print(ans)