import sys
sys.stdin=open('input 2573.txt','r')
# 통과
from sys import stdin
from collections import deque
input = stdin.readline

n, m = [int(x) for x in input().rstrip().split()]
L=[]
k = 0
V=[]
for i in range(n):
    L.append([*map(int,input().split())])
    for j in L[-1]:
        if j:
            k+=1
            V.append((i,j))
k2=k
def bfs(i,j):
    global k2
    V = {(i, j)}  # V가 리스트이면 시간초과!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    q = deque([(i, j)])
    while q: # 빙산이 한덩어리로 주어지므로
        i, j = q.popleft()
        # 동서남북에서
        for di, dj in (-1, 0), (0, -1), (0, 1), (1, 0):
            ni,nj=i+di,j+dj
            if 0<=ni<n and 0<=nj<m:
                if not L[ni][nj] and (ni, nj) not in V: # L[ni][nj] 가 0 이하이고 V에 없으면 (빙산이 아니면)
                    if L[i][j]:
                        L[i][j]-=1 # 1 감소
                        if not L[i][j]:
                            k2-=1
                elif (ni,nj) not in V:
                    V.add((ni,nj))
                    q.append((ni,nj))
    return len(V)

def run():
    for i in range(n):
        for j in range(m):
            if L[i][j]:
                if k != bfs(i, j):
                    return True
                return False
    else:
        print(0)
        exit()

time = 0
while not run():
    k=k2
    time += 1
print(time)