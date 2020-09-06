import sys
sys.stdin=open('input.txt','r')

def up(i,j):
    if 0<=i-1:
        if L[i-1][j] in [1,2,5,6] and (i-1,j) not in V:
            return 1
    return 0

def down(i,j):
    if i+1<n:
        if L[i+1][j] in [1,2,4,7] and (i+1,j) not in V:
            return 1
    return 0

def right(i,j):
    if j+1<m:
        if L[i][j+1] in [1,3,6,7] and (i,j+1) not in V:
            return 1
    return 0

def left(i,j):
    if 0<=j-1:
        if L[i][j-1] in [1,3,4,5] and (i,j-1) not in V:
            return 1
    return 0

for t in range(int(input())):
    n,m,r,c,l=map(int,input().split())
    L=[[*map(int,input().split())] for _ in 'a'*n]
    S=[(r,c)]
    V={(r,c)}
    ans=0
    while S:
        if l==1:
            break
        l-=1
        a=len(S)
        for i in 'a'*a:
            d,e=S.pop(0)
            if L[d][e]==1:
                if up(d,e):
                    S.append((d-1,e))
                    V.add((d-1,e))
                if down(d,e):
                    S.append((d+1,e))
                    V.add((d+1,e))
                if right(d,e):
                    S.append((d,e+1))
                    V.add((d,e+1))
                if left(d,e):
                    S.append((d,e-1))
                    V.add((d,e-1))
            if L[d][e]==2:
                if up(d, e):
                    S.append((d - 1, e))
                    V.add((d - 1, e))
                if down(d, e):
                    S.append((d + 1, e))
                    V.add((d + 1, e))
            if L[d][e]==3:
                if right(d, e):
                    S.append((d, e + 1))
                    V.add((d, e + 1))
                if left(d, e):
                    S.append((d, e - 1))
                    V.add((d, e - 1))
            if L[d][e]==4:
                if up(d, e):
                    S.append((d - 1, e))
                    V.add((d - 1, e))
                if right(d, e):
                    S.append((d, e + 1))
                    V.add((d, e + 1))
            if L[d][e]==5:
                if right(d, e):
                    S.append((d, e + 1))
                    V.add((d, e + 1))
                if down(d, e):
                    S.append((d + 1, e))
                    V.add((d + 1, e))
            if L[d][e]==6:
                if down(d, e):
                    S.append((d + 1, e))
                    V.add((d + 1, e))
                if left(d, e):
                    S.append((d, e - 1))
                    V.add((d, e - 1))
            if L[d][e]==7:
                if left(d, e):
                    S.append((d, e - 1))
                    V.add((d, e - 1))
                if up(d,e):
                    S.append((d-1,e))
                    V.add((d-1,e))
    print('#%i'%(t+1),len(V))

