# 시간초과 (파이썬)
# 꾸역꾸역 돌아가는 느낌
# 50% 채점하는데 8분 ㄷㄷ
# w>=ans 일 때 제외해주니
# 50% 채점하는데 4분
# 틀림 (느낌이 10번 이하가 아니라 9번 이하로 해서 틀리느 느낌)
# 왜 9번 이하로 풀었을까?
# 이동하는 것을 다 2차원 리스트로 구현해서 시간이 오래 걸리는 듯
# 이동 끝나는 좌표만 잡아서 구현해야 빨리 끝날 듯
# 파이파이 성공
# 최소시간은 파이썬이 파이파이보다 빠름? 왜그렇지?
# 메모리 144392 kb
# 시간 3524 ms
# 1594 B


import sys
sys.stdin=open('../input.txt','r')

di=[-1,1,0,0]
dj=[0,0,-1,1]
def f(board,k):
    global R,B
    for y in range(n):
        for x in range(m):
            if board[y][x] == 'R':
                r = (y, x)
            if board[y][x] == 'B':
                b = (y, x)
   # R 움직이기 시도
    i,j=r
    ni,nj=i+di[k],j+dj[k]
    while board[ni][nj]=='.':
        board[i][j]='.'
        board[ni][nj]='R'
        i,j=ni,nj
        ni,nj=i+di[k],j+dj[k]
    r2=(i,j)
    if board[ni][nj]=='O':
         R+=1
         board[i][j]='.'
    # B 움직이기
    i,j=b
    ni,nj=i+di[k],j+dj[k]
    while board[ni][nj] == '.':
        board[i][j] = '.'
        board[ni][nj] = 'B'
        i, j = ni, nj
        ni, nj = i + di[k], j + dj[k]
    if board[ni][nj] == 'O':
        B+=1
        board[i][j]='.'
    # R 다시 움직이기
    i,j=r2
    ni,nj=i+di[k],j+dj[k]
    while board[ni][nj]=='.':
        board[i][j]='.'
        board[ni][nj]='R'
        i,j=ni,nj
        ni,nj=i+di[k],j+dj[k]
    if board[ni][nj]=='O':
         R+=1
         board[i][j]='.'
    return board

def g(board,k,w=1):
    global R, B, ans
    if w>ans:
        return
    if w<11:
        R=B=0
        board2=[i[:] for i in board]
        board3=f(board2,k)
        if B:
            return
        if R and not B:
            ans=min(ans,w)
            return
        if not R and not B:
            for z2 in range(4):
                g(board3,z2,w+1)
    else:
        return
n,m=map(int,input().split())
board=[[*input()]for _ in range(n)]
ans=9**9
R=B=0
for i in range(4):
    g(board,i,1)
if ans<9**9:
    print(ans)
else:
    print(-1)