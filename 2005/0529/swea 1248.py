import sys
sys.stdin=open('../input.txt', 'r')

def size(n):
    q=[n]
    cnt=0
    while q:
        cnt+=1
        a=q.pop()
        q.extend(V1[a])
    return cnt

for t in range(1, int(input())+1):
    v, e, n1, n2 = map(int, input().split())
    n3=9**9
    V1 = [[] for _ in range(v+1)]
    V2 = [[] for _ in range(v+1)]
    data = [*map(int, input().split())]
    for i in range(e):
        V1[data[2*i]].append(data[2*i+1])
        V2[data[2*i+1]].append(data[2*i])
    while n1 != n3:
        n1=V2[n1][0]
        n3=n2
        while n3>1 and n1 != n3:
            n3=V2[n3][0]
    print('#%i'%t, n1, size(n1))