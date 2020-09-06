import sys
sys.stdin=open('input.txt','r')
u=input;r=range
for t in r(int(u())):
    n,k=map(int,u().split())
    s=u();s+=s[:n//4-1];p=[]
    for i in r(n):p.append(int(s[i:i+n//4],16))
    p=sorted(list(set(p)));print('#%d %d'%(t+1,p[-k]))
