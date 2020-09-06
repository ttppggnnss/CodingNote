import sys
sys.stdin=open('../input.txt', 'r')

def size(n):
    q=[V[n]]
    cnt=0
    while q:
        a=q.pop()
        cnt+=1
        if a[0]!=0:
            q.append(V[a[0]])
        if a[1]!=0:
            q.append(V[a[1]])
    return cnt

for t in range(1, int(input())+1):
    v, e, n1, n2 = map(int, input().split())
    n3=9**9
    V = [[0, 0, 0] for _ in range(v+1)]
    data = [*map(int, input().split())]
    for i in range(e):
        if V[data[2*i]][0]==0:
            V[data[2*i]][0]=data[2*i+1]
        else:
            V[data[2*i]][1]=data[2*i+1]
        V[data[2*i+1]][2]=data[2*i]
    while n1 != n3:
        n1=V[n1][2]
        n3=n2
        while n3>1 and n1 != n3:
            n3=V[n3][2]
    print('#%i'%t, n1, size(n1))