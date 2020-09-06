import sys
sys.stdin=open('input.txt','r')
# 런타임 에러

def linked(j,i,L,V,cnt):
    V[j][i]=1
    cnt+=1
    for dy,dx in (1,0),(-1,0),(0,1),(0,-1):
        j2,i2=j+dy,i+dx
        if 0<=j2<y and 0<=i2<x:
            if L[j2][i2]>0 and V[j2][i2]<1:
                cnt=linked(j2,i2,L,V,cnt)
    return cnt

y, x = map(int,input().split())
L=[[*map(int,input().split())] for _ in [0]*y]
time=0

while 1:
    time+=1
    for i in range(x):
        for j in range(y):
            if L[j][i]>0:
                L[j][i]-=1
    V=[[0]*x for __ in [0]*y]
    nxt=[]
    for i in range(x):
        for j in range(y):
            if L[j][i]>0 and V[j][i]<1:
                cnt2=linked(j,i,L,V,0)
                nxt.append(cnt2)
    if len(nxt)>1:
        break
    if time>10:
        time=0
        break
print(time)
