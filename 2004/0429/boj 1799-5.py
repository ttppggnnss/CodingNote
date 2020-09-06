import sys
sys.stdin=open('../input.txt','r')

def solve1(p,z):
    global ans1
    ans1=max(len(p),ans1)
    for z2 in range(z,len(board2)):
        i,j=board2[z2]
        if i-j not in visit1 and i+j not in visit2:
            visit1.append(i-j)
            visit2.append(i+j)
            solve1(p+[(i,j)],z2+1)
            visit1.pop()
            visit2.pop()

def solve2(p,z):
    global ans2
    ans2=max(len(p),ans2)
    for z2 in range(z,len(board3)):
        i,j=board3[z2]
        if i-j not in visit3 and i+j not in visit4:
            visit3.append(i-j)
            visit4.append(i+j)
            solve2(p+[(i,j)],z2+1)
            visit3.pop()
            visit4.pop()

n=int(input())
board=[]
board2=[]
board3=[]
visit1=[]
visit2=[]
visit3=[]
visit4=[]
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