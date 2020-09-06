import sys
sys.stdin=open('input.txt','r')
# 틀림

y, x = map(int,input().split())
L=[[*map(int,input().split())] for _ in[0]*y]
time=0
while 1:
    # 1년 뒤 빙하 녹는다
    time+=1
    for i in range(x):
        for j in range(y):
            if L[j][i]>0:
                L[j][i]-=1
    V=[[0]*x for _ in [0]*y]
    q=[(0,0)]
    nxt=[]
    while q:
        y0,x0=q.pop()
        for dx,dy in (1,0),(-1,0),(0,1),(0,-1):
            nx,ny=x0+dx,y0+dy
            if 0<=nx<x and 0<=ny<y:
                if L[ny][nx]==0:
                    L[ny][nx]=-1
                    q.append((ny,nx))
                elif L[ny][nx]>0 and V[ny][nx]<1:
                    q2=[(ny,nx)]
                    V[ny][nx]=1
                    cnt=1
                    while q2:
                        y1,x1=q2.pop()
                        for dx2,dy2 in  (1,0),(-1,0),(0,1),(0,-1):
                            nx2,ny2=x1+dx2,y1+dy2
                            if 0<=nx2<x and 0<=ny2<y:
                                if L[ny2][nx2]>0 and V[ny2][nx2]<1:
                                    q2.append((ny2,nx2))
                                    V[ny2][nx2]=1
                                    cnt+=1
                    if cnt>0:
                        nxt.append(cnt)
    for i in range(x):
        for j in range(y):
            if L[j][i]<0:
                L[j][i]=0
    if len(nxt)>1:
        break
    if time>10:
        time=0
        break
print(time)