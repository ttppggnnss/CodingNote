# pypy 통과
# python3 시간초과
import sys
sys.stdin=open('../input.txt','r')

for t in range(int(input())):
    w,h=map(int,input().split())
    fire=[]
    building=[]
    now=[]
    ans='IMPOSSIBLE'
    for i in range(h):
        building.append([*input()])
        for j in range(w):
            if building[i][j]=='*':
                fire.append((i,j))
            if building[i][j]=='@':
                building[i][j]='X'
                now.append((i,j))

    dy=[0,0,1,-1]
    dx=[1,-1,0,0]
    cnt=0
    z=0
    while now:
        new_fire=[]
        new_now=[]
        for a in fire:
            i,j=a
            for k in range(4):
                ni,nj=i+dy[k],j+dx[k]
                if -1<ni<h and -1<nj<w and (building[ni][nj]=='.' or building[ni][nj]=='X'):
                    building[ni][nj]='*'
                    new_fire.append((ni,nj))
        for b in now:
            i,j=b
            if i==0 or j==0 or i==h-1 or j==w-1:
                z=1
                break
            for k in range(4):
                ni, nj = i + dy[k], j + dx[k]
                if -1 < ni < h and -1 < nj < w and building[ni][nj] == '.':
                    building[ni][nj] = 'X'
                    new_now.append((ni, nj))
        cnt+=1
        fire=new_fire
        now=new_now
        if z:
            ans=cnt
            break
    print(ans)