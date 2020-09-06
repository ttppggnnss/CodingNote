import sys
sys.stdin=open('input.txt','r')

def f(j,i):
    y,x=0,0
    while M[j+y][i]:
        y+=1
    while M[j][i+x]:
        x+=1
    for q in range(y):
        for p in range(x):
            V[j+q][i+p]=1
    return (y,x)
for t in range(1,int(input())+1):
    n=int(input())
    M=[[*map(int,input().split())]for _ in[0]*n]
    V=[[0]*n for _ in [0]*n]
    ans=[]
    for i in range(n):
        for j in range(n):
            if M[j][i] and V[j][i]<1:
                ans.append(f(j,i))
    print("#%i"%t,len(ans),*sum(sorted(ans,key=lambda x:(x[0]*x[1],x[0])),()))

