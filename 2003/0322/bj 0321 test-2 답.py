import sys
from collections import deque
input = sys.stdin.readline

EMPTY, GREEN, RED, FLOWER = 0, 1, 2, 3
n,m,g,r = 0, 0, 0, 0
board = []
dx = [1,0,-1,0]
dy = [0,1,0,-1]
cand = [] # 좌표를 담을 에정
candsz = 0
isused = [False]*10
chosen_g = [0]*5
chosen_r = [0]*5
mx = 0

# popleft, append
def solve():
  cnt = 0
  state = [[[0]*2 for i in range(m)] for j in range(n)]
  q = deque()

  for i in range(g):
    state[cand[chosen_g[i]][0]][cand[chosen_g[i]][1]] = [0, GREEN]
    q.append(cand[chosen_g[i]])

  for i in range(r):
    state[cand[chosen_r[i]][0]][cand[chosen_r[i]][1]] = [0, RED]
    q.append(cand[chosen_r[i]])

  while q:
    cur = q.popleft()
    curtime, curcolor = state[cur[0]][cur[1]]
    if state[cur[0]][cur[1]][1] == FLOWER: continue
    for dir in range(4):
      nx = cur[0]+dx[dir]
      ny = cur[1]+dy[dir]
      if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
      if board[nx][ny] == 0: continue
      if state[nx][ny][1] == EMPTY:
        state[nx][ny] = [curtime+1,curcolor]
        q.append([nx,ny])
      elif state[nx][ny][1] == RED:
        if curcolor == GREEN and state[nx][ny][0] == curtime+1:
          cnt += 1
          state[nx][ny][1] = FLOWER
      elif state[nx][ny][1] == GREEN:
        if curcolor == RED and state[nx][ny][0] == curtime+1:
          cnt += 1
          state[nx][ny][1] = FLOWER
  return cnt

def select_r(idx):
  global mx
  if idx == r:
    mx = max(mx, solve())
    return None

  cur = 0
  if idx != 0: cur = chosen_r[idx-1] + 1
  while cur < candsz:
    if isused[cur]:
      cur += 1
      continue
    isused[cur] = True
    chosen_r[idx] = cur
    select_r(idx+1)
    isused[cur] = False
    cur += 1

def select_g(idx):
  if idx == g:
    select_r(0)
    return None

  cur = 0
  if idx != 0: cur = chosen_g[idx-1] + 1
  while cur < candsz:
    isused[cur] = True
    chosen_g[idx] = cur
    select_g(idx+1)
    isused[cur] = False
    cur += 1

n,m,g,r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
  for j in range(m):
    if board[i][j] == 2:
      cand.append([i,j])
candsz = len(cand)
select_g(0)
sys.stdout.write(str(mx)+"\n")