import sys
sys.stdin=open('../input.txt','r')

def DFS(tree):
    stack = [0]
    n = 1
    for t in tree:
        if t == '0':
            stack.append(n)
            lst.append(n)
            n += 1
        else:
            k = stack.pop()
            lst.append(k)
            parents[k] = stack[-1]

input = sys.stdin.readline

N = int(input())
tree = input().strip()
X, Y = map(int, input().split())
lst = [0]
parents = [0 for _ in range(N+1)]
DFS(tree)

checkx = lst[X]
checky = lst[Y]
X_parents = [checkx]
Y_parents = [checky]

while parents[checkx]:
    X_parents.append(parents[checkx])
    checkx = parents[checkx]
while parents[checky]:
    Y_parents.append(parents[checky])
    checky = parents[checky]

lca = 1
for x in X_parents:
    for y in Y_parents:
        if x == y:
            if lca < x:
                lca = x
dx = dy = -1

for i in range(len(lst)):
    if lst[i] == lca and dx == -1:
        dx = i
    elif lst[i] == lca and dy == -1:
        dy = i
print(dx, dy)