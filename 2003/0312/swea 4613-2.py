import sys
sys.stdin=open('input.txt','r')

def f(i,c):return m-i.count(c)
def d(c,cn,co):
    global a,ch
    i=ch[c]
    if c==n-1:
        if co=='R':
            cn+=i[2]
            if a>cn:ans=cn
            a=min(a,cn)
        return
    if co=='W':d(c+1,cn+i[0],'W');d(c+1,cn+i[0],'B')
    if co=='B':d(c+1,cn+i[1],'B');d(c+1,cn+i[1],'R')
    if co=='R':d(c+1,cn+i[2],'R')
for t in range(1,int(input())+1):
    n,m=map(int,input().split());fl=[[*input()]for _ in'a'*n];ch=[]
    for i in fl:ch.append([f(i,'W'),f(i,'B'),f(i,'R')])
    a=9**9;d(0,0,'W');print('#%i'%t,a)