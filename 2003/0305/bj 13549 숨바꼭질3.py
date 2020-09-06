import sys
from collections import deque
sys.stdin=open('input.txt','r')
input=sys.stdin.readline

def f(n,k,ans=0):
    global ans2
    q=deque()
    d=n
    for i in range(1,min(100001,2*k)):
        if i%d==0:
            q.append(i)
            v[i]=1
            d=2*d
    if k not in q:

        while 1:
            ans+=1
            for j in range(len(q)):
                a=q.popleft()
                b=a+1
                c=a-1
                for i in range(1,min(100001,2*k)):
                    if i%b==0 and v[i]<1:
                        q.append(i);v[i]=1;b=2*b
                for i in range(1,min(100001,2*k)):
                    if i%c==0 and v[i]<1:
                        q.append(i);v[i]=1;c=2*c
            if k in q:
                ans2=q.count(k)
                return ans
    else:
        return 0

n,k=map(int,input().split())
v=[0]*100001
ans2=1
print(f(n,k))