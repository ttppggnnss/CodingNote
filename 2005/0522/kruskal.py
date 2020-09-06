import sys
sys.stdin=open('../input.txt', 'r')

def make_set(x):
    p[x] = x

def find_set(x):
    if p[x] == x : return x
    else:
        p[x] = find_set(p[x])

def union(x, y):
    px = find_set(x)
    py = find_set(y)
    if rank[px] > rank[py]:
        p[py] = px
    else:
        p[px] = py
        if rank[px] == rank[py]:
            rank[py] += 1


V, E = map(int,input().split())
edges = [list(map(int, input().split())) for  i in range(E)]
# 간선 가중치 기준으로 정렬
edges.sort(key=lambda x:x[2])
p = [0] * V
rank = [0] * V
for i in range(V):
    make_set(i)

cnt = 0
result = 0
mst = []
for i in range(E):
    s, e, c = edges[i][0], edges[i][1], edges[i][2]
    if find_set(s) == find_set(e):
        continue
    result += c
    mst.append(edges[i])
    union(s,e)
    cnt+=1
    if cnt == V-1 : break