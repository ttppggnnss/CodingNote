# pypy 통과
# python3 시간초과
import sys
sys.stdin=open('../input.txt','r')
from collections import deque
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
for t in range(int(input())):
    w,h=map(int,input().split())
    building=[]
    fire=deque()
    now=deque()
    ans='IMPOSSIBLE'
    cnt=0;z=0
    for i in range(h):
        building.append([*input()])
        for j in range(w):
            if building[i][j]=='*':
                fire.append((i,j))
            if building[i][j]=='@':
                building[i][j]='X'
                now.append((i,j))
    while now:
        cnt+=1
        for a in range(len(fire)):
            i,j=fire.popleft()
            for k in range(4):
                ni,nj=i+dy[k],j+dx[k]
                if -1<ni<h and -1<nj<w and (building[ni][nj]=='.' or building[ni][nj]=='X'):
                    building[ni][nj]='*'
                    fire.append((ni,nj))
        for b in range(len(now)):
            i,j=now.popleft()
            if i==0 or j==0 or i==h-1 or j==w-1:
                z=1
                break
            for k in range(4):
                ni, nj = i + dy[k], j + dx[k]
                if -1 < ni < h and -1 < nj < w and building[ni][nj] == '.':
                    building[ni][nj] = 'X'
                    now.append((ni, nj))
        if z:
            ans=cnt
            break
    print(ans)