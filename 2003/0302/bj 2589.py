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
    if cnt<=2:
        return True
    else:
        return False
def check2(S,G,cnt=0):
    cnt2=0
    i,j=S
    if S==G:
        global ans
        ans=max(ans,cnt)
        print(ans)
        return cnt
    V[i][j]=1
    for di, dj in D:
        ni, nj = i + di, j + dj
        if 0 <= ni < y and 0 <= nj < x:
            if M[ni][nj] == 'L' and V[ni][nj] < 1:
                V[ni][nj]=1
                cnt2=check2((ni,nj),G,cnt+1)
                V[ni][nj]=0
    return cnt2
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
for a in range(r-1):
    for b in range(a+1,r):
        S=L2[a]
        G=L2[b]
        V = [[0] * x for _ in 'a' * y]
        check2(S,G)
print(ans)