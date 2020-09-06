import sys
sys.stdin=open('input.txt','r')
input=sys.stdin.readline

D=(1,0),(-1,0),(0,1),(0,-1)
def check(s):
    cnt=0
    i,j=s
    for di,dj in D:
        ni,nj=i+di,j+dj
        if 0<=ni<y and 0<=nj<x:
            if M[ni][nj]=='L':
                cnt+=1
    if cnt==1:
        return True
    else:
        return False
def check2(S,cnt=-1):
    i,j=S
    print(S)
    if (i,j)in G:
        return cnt
    V[i][j] = 1
    for di, dj in D:
        ni, nj = i + di, j + dj
        if 0 <= ni < y and 0 <= nj < x:
            if M[ni][nj] == 'L' and V[ni][nj] < 1:
                V[ni][nj]=1
                cnt=check2((ni,nj),cnt+1)
                V[ni][nj]=0
    return 0

y,x = map(int,input().split())
M=[[*input()] for _ in'a'*y]
L=[]
L2=[]
for i in range(y):
    for j in range(x):
        if M[i][j]=='L':
            L.append((i,j))
            if check((i,j)):
                L2.append((i,j))
ans=0
r=len(L2)
for a in range(r):
    V = [[0] * x for _ in 'a' * y]
    G=[i for i in L2]
    G.pop(a)
    h=check2(L2[a])
    print(h)
    if h>ans:
        ans=h
print(ans)