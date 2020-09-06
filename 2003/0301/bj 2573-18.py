# 시간 초과 수정하기
# 시간 초과
import sys
sys.stdin=open('input.txt','r')
input=sys.stdin.readline
def cnt0(i,j):
    cnt=0
    if L[i+1][j]<1 and (i+1,j) not in r:
            cnt+=1
    if L[i-1][j]<1 and (i-1,j) not in r:
            cnt+=1
    if L[i][j+1]<1 and (i,j+1) not in r:
            cnt+=1
    if L[i][j-1]<1 and (i,j-1) not in r:
            cnt+=1
    return cnt

n,m=map(int,input().split())
L=[]
k=0
for i in range(n):
    L.append([*map(int,input().split())])
    k+=m-L.count(0)
time=0
while 1:
    time+=1
    q=[]
    r=[]
    for i in range(n):
        for j in range(m):
            if L[i][j]>0:
                L[i][j]-=cnt0(i,j)
                if L[i][j]>0:q.append((i,j))
                else:r.append((i,j))
    if k!=len(q):
        k=len(q)
        if q:
            p=[q.pop()]
            # for i in p:
            while p:
                y,x=p.pop()
                # y,x=i
                if (y+1,x) in q:
                    q.remove((y+1,x))
                    p.append((y+1,x))
                if (y-1,x) in q:
                    q.remove((y-1,x))
                    p.append((y-1,x))
                if (y,x+1) in q:
                    q.remove((y,x+1))
                    p.append((y,x+1))
                if (y,x-1) in q:
                    q.remove((y,x-1))
                    p.append((y,x-1))
        else:
            print(0)
            break
        if q:
            print(time)
            break
