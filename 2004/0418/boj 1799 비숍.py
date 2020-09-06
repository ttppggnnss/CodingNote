import sys
sys.stdin=open('../input.txt','r')

def check(i,j):
    if i==0:
        return True
    else:
        for k in range(1,i+1):
            if i-k>-1 and j-k>-1 and visit[i-k][j-k]>0:
                return False
            if i-k>-1 and j+k<n and visit[i-k][j+k]>0:
                return False
        else:
            return True

n=int(input())
board=[[*map(int,input().split())]for _ in range(n)]
visit=[[0]*n for _ in range(n)]
cnt=0
for i in range(n):
    for j in range(n):
        if board[i][j]>0 and visit[i][j]<1:
            if check(i,j):
                visit[i][j]=1
                cnt+=1
print(cnt)