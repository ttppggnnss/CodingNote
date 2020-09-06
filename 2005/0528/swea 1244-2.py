import sys
sys.stdin=open('../input.txt', 'r')

for t in range(1, int(input()) + 1):
    a, b = input().split()
    b = int(b)
    q = [[i for i in a]]
    while b>0:
        nxt=[]
        while q:
            a2=q.pop()
            a3=[i for i in a2]
            for i in range(len(a2)-1):
                for j in range(i+1,len(a2)):
                    a2[i], a2[j] = a2[j], a2[i]
                    if a2 not in nxt:
                        nxt.append(a2)
                    a2=[k for k in  a3]
        ans = [int(''.join(i)) for i in nxt]
        b-=1
        q=[i for i in nxt]
    print('#%i'%t, max(ans))
