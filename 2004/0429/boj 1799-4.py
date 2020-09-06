import sys
sys.stdin=open('../input.txt','r')

def check(i,j,p):
    for k in range(i+1):
        if i-k>-1 and j-k>-1 and (i-k,j-k) in p:
            return False
        if i-k>-1 and j+k<n and (i-k,j+k) in p:
            return False
    return True

def solve1(p,z):
    global ans1
    ans1=max(len(p),ans1)
    for z2 in range(z,len(board2)):
        i,j=board2[z2]
        if check(i,j,p):
            solve1(p+[(i,j)],z2+1)

def solve2(p,z):
    global ans2
    ans2=max(len(p),ans2)
    for z2 in range(z,len(board3)):
        i,j=board3[z2]
        if check(i,j,p):
            solve2(p+[(i,j)],z2+1)

n=int(input())
board=[]
board2=[]
board3=[]
for i in range(n):
    board.append([*map(int,input().split())])
    for j in range(n):
        if board[i][j]==1 and (i+j)%2==1:board2.append((i,j))
        if board[i][j]==1 and (i+j)%2==0:board3.append((i,j))
ans1=0
ans2=0
solve1([],0)
solve2([],0)
print(ans1+ans2)