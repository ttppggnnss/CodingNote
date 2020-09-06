# 숏코딩
import sys
sys.stdin=open('input2.txt','r')

Y=[-1,1,0,0]
X=[0,0,-1,1]
for t in range(1,int(input())+1):
    h,w=map(int,input().split());T='^v<>';e={'U':0,'D':1,'L':2,'R':3};b=[]
    for i in range(h):
        b.append([*input()])
        for j in range(w):
            if b[i][j] in T:y,x=i,j;D=T.index(b[i][j])
    n=int(input());o=input()
    for c in o:
        if c=='S':
            p,q=y+Y[D],x+X[D]
            while -1<p<h and -1<q<w:
                if b[p][q]=='#':break
                if b[p][q]=='*':b[p][q]='.';break
                p,q=p+Y[D],q+X[D]
        else:
            d=e[c];p,q=y+Y[d],x+X[d]
            if -1<p<h and -1<q<w and b[p][q]=='.':b[y][x]='.';b[p][q]=T[d];y,x=p,q;D=d
            else:b[y][x]=T[d];D=d
    print('#%i'%t,end=" ")
    for i in b:print(*i,sep='')
    # for i in b:print(''.join(i)) 시간은 이게 더 빠름 메모리도 덜 씀