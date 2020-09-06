import sys
sys.stdin=open('input.txt','r')

def f(j,i):
    y,x=0,0
    while M[j+y][i]:y+=1
    while M[j][i+x]:x+=1
    for p in range(y):
        for q in range(x):M[j+p][i+q]=0
    return (y,x)
for t in range(1,int(input())+1):
    n=int(input());ans=[];M=[[*map(int,input().split())]for _ in[0]*n]
    for i in range(n):
        for j in range(n):
            if M[j][i]:ans.append(f(j,i))
    print("#%i"%t,len(ans),*sum(sorted(ans,key=lambda x:(x[0]*x[1],x[0])),()))
