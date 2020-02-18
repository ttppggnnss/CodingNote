def bt(y,x):
    k=1
    for dx,dy in (-1,-1),(0,-1),(1,-1):
        nx,ny=x+dx,y+dy
        while 0<=nx<n and 0<=ny<n:
            if V[ny][nx]==1:
                k=0;return
            nx+=dx;ny+=dy
    if k:
        y+=1
        if y==n:
            global ans
            ans+=1;return
        for x in range(n):
            V[y][x]=1
            bt(y,x)
            V[y][x]=0

n=int(input())
V=[[0]*n for _ in[0]*n]
ans=0
for i in range(n):
    V[0][i]=1
    bt(0,i)
    V[0][i]=0
print(ans)