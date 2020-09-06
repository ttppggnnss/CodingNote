# https://www.acmicpc.net/problem/2573
# 빙산
# 시간초과

import sys
sys.stdin=open('input.txt','r')

y, x = map(int,input().split())
L=[[*map(int,input().split())] for _ in[0]*y]
time=0
while 1:
    # 1년 뒤 빙하 녹는다
    time+=1
    for i in range(x):
        for j in range(y):
            L[j][i]-=1
    # -1이면 0으로 바꿔준다
    nxt=[]
    q=[(0,0)]
    L2 = [[0] * len(L[0]) for _ in [0] * len(L)]
    # L2 가 visited 역할
    while q:
        y0, x0 = q.pop()
        for dy, dx in (1, 0), (-1, 0), (0, 1), (0, -1):
            nx, ny = x0 + dx, y0 + dy
            if 0 <= nx < len(L[0]) and 0 <= ny < len(L):
                if L[ny][nx] == -1:
                    L[ny][nx] = 0
                    q.append((ny, nx))
                # 0보다 크면 연결된 점들 이어서 카운트한다
                # L2 를 조작한다
                elif L[ny][nx] > 0:
                    q2=[(ny,nx)]
                    cnt=0
                    while q2:
                        y1,x1=q2.pop()
                        for dy2, dx2 in (0, 1), (0, -1), (1, 0), (-1, 0):
                            nx2, ny2 = x1 + dx2, y1 + dy2
                            if 0 <= ny2 < y and 0 <= nx2 < x:
                                if L[ny2][nx2]>0 and L2[ny2][nx2]==0:
                                    L2[ny2][nx2]=1
                                    q2.append((ny2, nx2))
                                    cnt += 1
                    if cnt!=0:
                        nxt.append(cnt)
    if len(nxt)>1:
        break
print(time)