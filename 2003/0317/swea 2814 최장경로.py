import sys
sys.stdin=open('input.txt','r')

def bt(ans,cnt,j):
    if ans<cnt:ans=cnt
    for i in L[j]:
        if i not in V:
            V.add(i);cnt+=1
            ans=bt(ans,cnt,i)
            V.remove(i);cnt-=1
    return ans
for t in range(1,int(input())+1):
    n,m=map(int,input().split())
    L=[[]for _ in'a'*(n+1)]
    for _ in 'a'*m:
        a,b=map(int,input().split())
        L[a].append(b)
        L[b].append(a)
    V=set();ans=1;cnt=0
    for i in range(n):
        for j in L[i]:
            V.add(j);cnt+=1
            ans=bt(ans,cnt,j)
            cnt-=1;V.remove(j)
    print('#%i'%t,ans)