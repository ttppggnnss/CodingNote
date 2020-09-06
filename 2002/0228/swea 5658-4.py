# 황수현 풀이 참고
import sys
sys.stdin=open('input.txt','r')
I=int;u=input;r=range
for t in r(1,I(u())+1):
    n,k=map(I,u().split());s=u();s+=s+s[:n//4-1];p=[]
    for i in r(n):p.append(I(s[i:i+n//4],16))
    p=sorted(list(set(p)));print("#%d %d"%(t,p[-k]))