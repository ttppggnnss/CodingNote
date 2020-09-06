# 시간 초과
# 시간 제한이 1초라 어려움
import datetime
start=datetime.datetime.now()
print(datetime.datetime.now()-start)
import sys
sys.stdin=open('input.txt','r')

import sys
input=sys.stdin.readline
y, x = map(int,input().split())
L=[[*map(int,input().split())] for _ in[0]*y]
time=0
q={}
for i in range(x):
    for j in range(y):
        if L[j][i]>0:
            q[(j,i)]=L[j][i]
while 1:
    time+=1
    qr=[]
    for i in q:
        q[i]-=1
        if q[i]==0:
            qr.append(i)
    for i in qr:
        del q[i]
    nxt=[list(q)[0]]
    while 1:
        a=len(nxt)
        for i in q:
            for dx,dy in (1,0),(-1,0),(0,1),(0,-1):
                j=i[0]+dy,i[1]+dx
                if j in nxt and i not in nxt:
                    nxt.append(i)
        b=len(nxt)
        if a==b:
            break
    if len(nxt)<len(q):
        break
    if time>10:
        time=0
        break
print(time)
print(datetime.datetime.now()-start)




