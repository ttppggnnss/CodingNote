import sys
sys.stdin=open('input.txt','r')

for t in range(1,int(input())+1):
    n,m=map(int,input().split());b=[[0]*n for _ in'a'*n];p=n>>1;b[p][p]=2;b[p-1][p]=1;b[p][p-1]=1;b[p-1][p-1]=2
    for _ in range(m):
        y,x,c=map(int,input().split());y-=1;x-=1;b[y][x]=c
        for i in 0,-1,1:
            for j in 0,1,-1:
                Y=y+i;X=x+j;k=0
                while not(i==j==0)and -1<Y<n and -1<X<n:
                    k+=1
                    if b[Y][X]<1:break
                    if b[Y][X]==c:
                        for q in range(k):b[y+i*q][x+j*q]=c
                        break
                    Y+=i;X+=j
    print("#%d"%t,sum(1for i in sum(b,[])if i==1),sum(1for i in sum(b,[])if i==2))