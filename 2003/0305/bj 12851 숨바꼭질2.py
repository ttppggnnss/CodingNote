import sys
from collections import deque
sys.stdin=open('input.txt','r')
input=sys.stdin.readline

def f(n,k,ans=0):
    global ans2
    q=deque([n])
    v[n]=1
    if n!=k:
        while 1:
            ans+=1
            for j in range(len(q)):
                i=q.popleft()
                v[i]=1
                if i+1<100001 and v[i+1]<1:q.append(i+1)
                if i-1>-1 and v[i-1]<1:q.append(i-1)
                if 2*i<100001 and v[2*i]<1:q.append(2*i)
            if k in q:
                ans2=q.count(k)
                return ans
    else:
        return 0

n,k=map(int,input().split())
v=[0]*100001
ans2=1
print(f(n,k))
print(ans2)