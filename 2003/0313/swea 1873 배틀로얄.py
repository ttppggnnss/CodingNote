import sys
sys.stdin=open('input2.txt','r')

dy=[-1,1,0,0]
dx=[0,0,-1,1]
for t in range(1,int(input())+1):
    h,w=map(int,input().split())
    tank='^v<>'
    nswe={'U':0,'D':1,'L':2,'R':3}
    b=[]
    for i in range(h):
        b.append([*input()])
        for j in range(w):
            if b[i][j] in tank:
                y,x=i,j
                td=tank.index(b[i][j])
    n=int(input())
    o=input()
    for cmd in o:
        if cmd=='S':
            ty=y+dy[td]
            tx=x+dx[td]
            while -1<ty<h and -1<tx<w:
                if b[ty][tx]=='#':break
                if b[ty][tx]=='*':b[ty][tx]='.';break
                ty,tx=ty+dy[td],tx+dx[td]
        else:
            d=nswe[cmd]
            ty,tx=y+dy[d],x+dx[d]
            if -1<ty<h and -1<tx<w and b[ty][tx]=='.':
                b[y][x]='.'
                b[ty][tx]=tank[d]
                y,x=ty,tx
                td=d
            else:
                b[y][x]=tank[d]
                td=d
    print('#%i'%t,end=" ")
    for i in b:print(''.join(i))


