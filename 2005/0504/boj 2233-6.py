import sys
input=sys.stdin.readline
n=int(input())
s=input()
x,y=map(int,input().split())
S=[0];T=[0];a=0;P=0
for i in range(len(s)):
    if s[i]=='0':
        a+=1
        T.append(a)
        S.append(a)
        if i==x-1 and i==y-1:X=S[:][::-1];Y=S[:][::-1]
        if i==x-1 and i!=y-1:X=S[:][::-1]
        if i==y-1 and i!=x-1:Y=S[:][::-1]
    else:
        if i==x-1 and i== y-1:X=S[:][::-1];Y=S[:][::-1]
        if i==x-1 and i!=y-1:X=S[:][::-1]
        if i==y-1 and i!=x-1:Y=S[:][::-1]
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