import sys
sys.stdin=open('input.txt','r')

def f(i,j,p,cnt=0):
    global ans
    if cnt==7:ans+=[p];return
    p+=b[i][j]
    if i>0:f(i-1,j,p,cnt+1)
    if j>0:f(i,j-1,p,cnt+1)
    if i<3:f(i+1,j,p,cnt+1)
    if j<3:f(i,j+1,p,cnt+1)
for t in range(1,1+int(input())):
    b=[input().split() for _ in'a'*4];ans=[]
    for i in range(4):
        for j in range(4):f(i,j,'')
    print('#%i'%t,len(set(ans)))