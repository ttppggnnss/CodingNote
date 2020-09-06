import sys
sys.stdin=open('../input.txt','r')

def visit(i,j,chess_board):
    for di,dj in (1,-1),(1,0),(1,1):
        ni,nj=i+di,j+dj
        while ni<n and -1<nj<n:
            chess_board[ni][nj]=1
            ni,nj=ni+di,nj+dj

def bt(i,n,chess_board):
    global ans
    if i==n:ans+=1;return
    for j in range(n):
        if chess_board[i][j]<1:
            chess_board2 = [a[:] for a in chess_board]
            visit(i,j,chess_board2)
            bt(i+1,n,chess_board2)

for t in range(1,int(input())+1):
    n=int(input());ans=0
    chess_board=[[0]*n for _ in'a'*n]
    bt(0,n,chess_board)
    print('#%i'%t,ans)
