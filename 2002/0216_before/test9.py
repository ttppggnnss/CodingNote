import sys;sys.stdin=open('input9.txt','r')

def bf(v2,res):
    if v2==v:
        global ans
        ans.append(res)
    for i in range(v+1):
        if L[i][v2]!=0:
            res+=L[i][v2]
            constant=L[i][v2]
            L[i][v2] = 0
            bf(i,res)
            L[i][v2] = constant
            res-=constant

for t in range(1,int(input())+1):
    v,e = map(int,input().split())
    L=[[0]*(v+1) for _ in [0]*(v+1)]
    for _ in [0] * e:
        v1, v2, cost = map(int, input().split())
        L[v2][v1] = cost
    L2=list(zip(*L))

    ans=[]
    bf(0,0)
    print("#%i"%t,min(ans))