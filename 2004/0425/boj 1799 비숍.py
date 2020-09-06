# 메모리 초과
import sys
sys.stdin=open('../input.txt','r')

def check(i,j,p):
    for k in range(i+1):
        if i-k>-1 and j-k>-1 and (i-k,j-k) in p:
            return False
        if i-k>-1 and j+k<n and (i-k,j+k) in p:
            return False
    return True

n=int(input())
board=[[*map(int,input().split())]for _ in range(n)]
ans=0
p=[]
q=[]
q.append([p,0])
for i in range(n):
    for j in range(n):
        if board[i][j]>0:
            for z in range(len(q)):
                k=q[z]
                if check(i,j,k[0]):
                    q.append([k[0]+[(i,j)],k[1]+1])
                    ans=max(ans,k[1]+1)
print(ans)