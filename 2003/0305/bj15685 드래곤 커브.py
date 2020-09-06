import sys
sys.stdin=open('input.txt','r')
input=sys.stdin.readline
dx,dy=[1,0,-1,0],[0,-1,0,1]
def dc(y,x,d,g,k=-1,q=[]):
    if k==g:
        for i in q:
            b[i[0]][i[1]]=1
        return
    if k==-1:
        q.append((y,x))
        q.append((y+dy[d],x+dx[d]))
        dc(y+dy[d],x+dx[d],d,g,k+1,q)
    else:
        for i in range(len(q)):
            if q[i]!=(y,x):
                q.append((y-x+q[i][1],x+y-q[i][0]))
        dc(y-x+q[0][1],x+y-q[0][0],d,g,k+1,q)

n=int(input());ans=0
b=[[0]*101 for _ in 'a'*101]
for i in 'a'*n:
    x,y,d,g=map(int,input().split())
    dc(y,x,d,g,-1,[])
for i in range(100):
    for j in range(100):
        if b[i][j] and b[i+1][j] and b[i][j+1] and b[i+1][j+1]:ans+=1
print(ans)
