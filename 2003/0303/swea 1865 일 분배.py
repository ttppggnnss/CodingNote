import sys
sys.stdin=open('input.txt','r')

def bt(res,num=0):
    global ans
    if num==n:
        ans=max(ans,res*100)
    if res*100<ans:
        return
    for i in range(n):
        if V[i]<1 and P[num][i]:
            res=res*P[num][i]/100
            V[i]=1
            bt(res,num+1)
            V[i]=0
            res=res*100/P[num][i]

for t in range(1,1+int(input())):
    n=int(input())
    P=[[*map(int,input().split())] for _ in 'a'*n]
    V=[0]*n
    ans=0
    bt(1)
    print('#%i %.6f'%(t,ans))