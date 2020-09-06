import sys
sys.stdin=open('../input.txt','r')



di=[1,-1,0,0]
dj=[0,0,1,-1]
visit2=[[0]*5 for _ in range(5)]
def isone(i,j):
    global cnt
    cnt+=1
    visit2[i][j]=1
    q=[(i,j)]
    while q:
        i,j=q.pop()
        for k in range(4):
            ni,nj=i+di[k],j+dj[k]
            if -1<ni<5 and -1<nj<5 and visit[ni][nj]==1 and visit2[ni][nj]<1:
                visit2[ni][nj]=1
                q.append((ni,nj))

def f(i,j,p,q):
    global cnt
    if len(p)==7:
        if p.count('S')>3:
            if visit not in visit3:
                visit3.append(visit[:])
        return
    for a,b in q:
        q2=[]
        for k in range(4):
            na,nb=a+da[k],b+db[k]
            q2.append((na,nb))
        if -1<a<5 and -1<b<5 and visit[a][b]<1:
            visit[a][b]=1
            p.append(board[a][b])
            f(a,b,p,q+q2)
            visit[a][b]=0
            p.pop()

board=[[*input()]for _ in range(5)]
visit=[[0]*5 for _ in range(5)]
visit3=[]
cnt
for i in range(5):
    for j in range(5):
        visit[i][j]=1
        f(i,j,[board[i][j]],[(i+1,j),(i-1,j),(i,j+1),(i,j-1)])
        visit[i][j]=0
print(len(visit3))