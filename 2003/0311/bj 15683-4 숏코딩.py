def f(y,x,D):
    s=set()
    for d in D:
        Y,X=y+i[d],x+j[d]
        while -1<Y<n and -1<X<m and b[Y][X]!=6:
            if b[Y][X]<1:s.add((Y,X))
            Y,X=Y+i[d],X+j[d]
    return s
def d(c,v):
    global M
    if c==len(t):M=max(len(v),M);return
    for o in t[c]:d(c+1,v|o)
i=[-1,0,1,0];j=[0,1,0,-1]
n,m=map(int,input().split());b=[[*map(int,input().split())]for _ in'a'*n];U,R,D,L = 0,1,2,3;a=0;t=[]
for y in range(n):
    for x in range(m):
        if b[y][x] == 1:t.append([f(y,x,[R]),f(y,x,[D]),f(y,x,[L]),f(y,x,[U])])
        if b[y][x] == 2:t.append([f(y,x,[U,D]),f(y,x,[R,L])])
        if b[y][x] == 3:t.append([f(y,x,[U,R]),f(y,x,[R,D]),f(y,x,[D,L]),f(y,x,[L,U])])
        if b[y][x] == 4:t.append([f(y,x,[U,R,D]),f(y,x,[R,D,L]),f(y,x,[D,L,U]),f(y,x,[L,U,R])])
        if b[y][x] == 5:t.append([f(y,x,[U,D,R,L])])
        if b[y][x]<1:a+=1
M=0;d(0,set());print(a-M)