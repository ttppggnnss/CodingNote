import sys
sys.stdin=open('input.txt','r')

def f(i,c):
    return m-i.count(c)

def d(c,cnt,color,L):
    global ans,change,L2
    if c==n-1:
        if color=='R':
            cnt+=change[n-1][2]
            L+=[color]
            if ans>cnt:
                ans=cnt
                L2=L
            ans=min(ans,cnt)
        return
    i=change[c]
    if color=='W':
        d(c+1,cnt+i[0],'W',L+[color])
        d(c+1,cnt+i[0],'B',L+[color])
    if color=='B':
        d(c+1,cnt+i[1],'B',L+[color])
        d(c+1,cnt+i[1],'R',L+[color])
    if color=='R':
        d(c+1,cnt+i[2],'R',L+[color])

for t in range(1,int(input())+1):
    n,m=map(int,input().split())
    flag=[[*input()]for _ in'a'*n]
    change=[]
    for i in flag:
        change.append([f(i,'W'),f(i,'B'),f(i,'R')])
    ans=9**9;L2=[]
    d(0,0,'W',[])
    print('#%i'%t,ans)