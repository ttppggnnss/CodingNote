import sys
sys.stdin=open('../input.txt','r')
input=sys.stdin.readline
def f(i,x,y):
    global X, Y
    if i==x-1 and i==y-1:X=S[:][::-1];Y=S[:][::-1]
    if i==x-1 and i!=y-1:X=S[:][::-1]
    if i==y-1 and i!=x-1:Y=S[:][::-1]
n=int(input())
s=input()
x,y=map(int,input().split())
S=[0];T=[0];a=0;P=0;X=[];Y=[]
for i in range(len(s)):
    if s[i]=='0':
        a+=1
        T.append(a)
        S.append(a)
        f(i,x,y)
    else:
        f(i,x,y)
        b=S.pop();T.append(b)
for i in X:
    for j in Y:
        if i==j:P=i;break
    if P:break
ans=[]
ans1=T.index(P)
ans.append(ans1)
try:ans.append(ans1+1+T[ans1+1:].index(P))
except:pass
print(*ans)