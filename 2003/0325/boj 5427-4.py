# python3 통과
import sys
sys.stdin=open('../input.txt','r')
dy=[0,0,-1,1]
dx=[1,-1,0,0]
def BFS(now,fire):
    cnt=0
    while now:
        new_fire = []
        new_now = []
        cnt+=1
        for k in fire:
            i,j=k
            for k2 in range(4):
                ni,nj=i+dy[k2],j+dx[k2]
                if -1<ni<h and -1<nj<w and (building[ni][nj]=='.'or building[ni][nj]=='@'):
                    building[ni][nj]='*'
                    new_fire.append((ni,nj))
        for k in now:
            i,j=k
            if i==0 or j==0 or i==h-1 or j==w-1:
                print(cnt)
                return
            for k2 in range(4):
                ni, nj = i + dy[k2], j + dx[k2]
                if -1 < ni < h and -1 < nj < w and building[ni][nj] == '.':
                    building[ni][nj] = '@'
                    new_now.append((ni, nj))
        now=new_now
        fire=new_fire
    print('IMPOSSIBLE')

for _ in range(int(input())):
    cnt = 0
    w,h=map(int,input().split())
    building=[]
    now=[]
    fire=[]
    for i in range(h):
        building.append([*input()])
        for j in range(w):
            if building[i][j]=='@':
                now.append([i,j])
            if building[i][j]=='*':
                fire.append([i,j])
    BFS(now,fire)