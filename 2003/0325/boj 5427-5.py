# python3 통과
import sys
sys.stdin=open('../input.txt','r')
def BFS(now,fire):
    cnt=0
    while now:
        new_fire=[]
        new_now=[]
        cnt+=1
        for k in fire:
            i,j=k
            if i<h-1 and building[i+1][j]=='.':building[i+1][j]='*';new_fire.append((i+1,j))
            if i>0 and building[i-1][j]=='.':building[i-1][j]='*';new_fire.append((i-1,j))
            if j<w-1 and building[i][j+1]=='.':building[i][j+1]='*';new_fire.append((i,j+1))
            if j>0 and building[i][j-1]=='.':building[i][j-1]='*';new_fire.append((i,j-1))
        for k in now:
            i,j=k
            if i==0 or j==0 or i==h-1 or j==w-1:print(cnt);return
            if i<h-1 and building[i+1][j]=='.':building[i+1][j]='@';new_now.append((i+1,j))
            if i>0 and building[i-1][j]=='.':building[i-1][j]='@';new_now.append((i-1,j))
            if j<w-1 and building[i][j+1]=='.':building[i][j+1]='@';new_now.append((i,j+1))
            if j>0 and building[i][j-1]=='.':building[i][j-1]='@';new_now.append((i,j-1))
        now=new_now
        fire=new_fire
    print('IMPOSSIBLE')
for _ in range(int(input())):
    w,h=map(int,input().split())
    building=[]
    now=[]
    fire=[]
    for i in range(h):
        building.append([*input()])
        for j in range(w):
            if building[i][j]=='@':now.append([i,j])
            elif building[i][j]=='*':fire.append([i,j])
    BFS(now,fire)