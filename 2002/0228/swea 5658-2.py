u=input;r=range
for t in r(int(u())):
    n,k=map(int,u().split())
    s=u();s+=s[:n//4-1];p=[]
    for i in r(n):
        a=int(s[i:i+n//4],16)
        if a not in p:p.append(a)
    p=sorted(p);print('#%d %d'%(t+1,p[-k]))