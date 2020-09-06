# 시간 초과

import sys
sys.stdin=open('input.txt','r')

y, x = map(int,input().split())
L=[[*map(int,input().split())] for _ in[0]*y]
time=0
q=[]
for i in range(x):
    for j in range(y):
        if L[j][i]>0:
            q.append((j,i))
while 1:
    time+=1
    qr=[]
    for i in q:
        L[i[0]][i[1]]-=1
        if L[i[0]][i[1]]==0:
            qr.append(i)
    for i in qr:
        q.remove(i)
    q2=[i for i in q]
    nxt=[q2.pop()]
    while 1:
        a=len(q2)
        for i in q2:
            for dx,dy in (1,0),(-1,0),(0,1),(0,-1):
                j=i[0]+dy,i[1]+dx
                if j in nxt and i not in nxt:
                    nxt.append(i)
                    q2.remove(i)
        b=len(q2)
        if a==b:
            break
    if len(nxt)<len(q):
        break
    if time>10:
        time=0
        break
print(time)





