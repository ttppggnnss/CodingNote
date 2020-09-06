import sys
sys.stdin=open('input.txt','r')

def bt(k,L,L2):
    global cnt
    for id,x in enumerate(L):
        L2.append(x)
        if sum(L2)>k:
            L2.remove(x)
            continue
        if sum(L2)<k:
            L4=L[id+1:]
            bt(k,L4,L2)
        if sum(L2)==k:
            cnt+=1
        L2.remove(x)
for t in range(1,int(input())+1):
    n, k = map(int,input().split())
    L=[*map(int,input().split())]
    cnt=0
    bt(k,L,[])
    print("#%i"%t, cnt)