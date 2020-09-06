# 틀림
import sys
sys.stdin=open('../input.txt','r')

def check(i,j,y,x,d):
    z2=0
    if (i+y)<=n and (j+x)<=m:
        for i2 in range(y):
            for j2 in range(x):
                if notebook[i+i2][j+j2]+sticker[d][i2][j2]>1:
                    z2=1
                    break
            if z2:
                break
    else:
        z2=1
    return 1-z2

n,m,k=map(int,input().split())
notebook=[[0]*m for _ in'a'*n]
ans=0
for _ in'a'*k:
    y,x=map(int,input().split())
    z=0
    sticker=[ [[*map(int,input().split())] for _ in'a'*y] ]
    sticker.append([list(k2)for k2 in zip(*sticker[-1][::-1])])
    sticker.append([list(k2)for k2 in zip(*sticker[-1][::-1])])
    sticker.append([list(k2)for k2 in zip(*sticker[-1][::-1])])
    for i in range(n):
        for j in range(m):
            for d in range(4):
                if check(i,j,y,x,d):
                    for i2 in range(y):
                        for j2 in range(x):
                            notebook[i+i2][j+j2]+=sticker[d][i2][j2]
                            ans+=sticker[d][i2][j2]
                    z=1
                    break
                x,y=y,x
            if z:
                break
        if z:
            break
print(ans)