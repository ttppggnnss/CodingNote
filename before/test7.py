S,C,U,D,m,n=[],{},{},{},0,int(input())
for i in range(n):C[i+1]=True
for i in range(2,2*n+1):U[i]=True
for i in range(1-n,n):D[i]=True
def f(x,z=n,y=1):
    for i in range(y,z+1):
        if C[i] and U[x+i] and D[x-i]:
            if x==n:
                global m
                m+=1
            else:
                C[i],U[x+i],D[x-i]=False,False,False
                S.append((x,i))
                f(x+1)
    if S:
        a,b=S.pop()
        C[b],U[a+b],D[a-b]=True,True,True

f(1,n//2)
m*=2
if n%2==1:f(1,n//2+1,n//2+1)
print(m)

