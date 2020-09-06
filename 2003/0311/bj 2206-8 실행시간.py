# 실행시간
import sys
sys.stdin=open('input.txt', 'r')

def bfs(aa, start_x, start_y):
	aa[start_x][start_y] = 1
	q = []
	q.append([start_x, start_y, aa[start_x][start_y]])
	while q:
		x = q[0][0]
		y = q[0][1]
		d = q[0][2]
		q.pop(0)
		for idx in [[1,0], [0,1], [-1,0], [0,-1]]:
			dx = x + idx[0]
			dy = y + idx[1]
			if not aa[dx][dy]:
				aa[dx][dy] = d+1
				q.append([dx, dy, d+1])

n,m=map(int,input().split())
a=[[-1]*(m+2)]
for i in range(n):
    s = input().strip()
    b=[-1]
    for i in s:
        if i == '0':
            b.append(0)
        else:
            b.append(-1)
    a.append(b)
    b.append(-1)
a.append([-1]*(m+2))
b = [i[:] for i in a]

bfs(a, 1, 1)
bfs(b, n, m)
chk = 0 if a[n][m] else 1
# chk : 막혀있음=1

if chk:
    res = 10000000
else:
    res = max(b[1][1], a[n][m])
for i in range(1, n+1):
	for j in range(1, m+1):
		if a[i][j] == -1:
			if	a[i-1][j] > 0 and b[i+1][j] > 0:
				chk = 0
				x = a[i-1][j]
				y = b[i+1][j]
				if x+y < res:	res = x+y+1
			if	a[i+1][j] > 0 and b[i-1][j] > 0:
				chk = 0
				x = a[i+1][j]
				y = b[i-1][j]
				if x+y < res:	res = x+y+1
			if	a[i][j-1] > 0 and b[i][j+1] > 0:
				chk = 0
				x = a[i][j-1]
				y = b[i][j+1]
				if x+y < res:	res = x+y+1
			if	a[i][j+1] > 0 and b[i][j-1] > 0:
				chk = 0
				x = a[i][j+1]
				y = b[i][j-1]
				if x+y < res:	res = x+y+1

if chk:
	print(-1)
else:
	if n == 1 and m == 1:
		res = 1
	print(res)
