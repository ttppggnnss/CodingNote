import sys
sys.stdin=open('../input.txt', 'r')

for t in range(1, int(input())+1):
    n=int(input())
    data=[]
    T=[0]*25
    ans=0
    for i in range(n):
        s,e=map(int,input().split())
        data.append((s,e))
    data=sorted(data, key=lambda x:x[1]-x[0])
    for i in data:
        if sum(T[i[0]:i[1]])==0:
            ans+=1
            for j in range(i[0],i[1]):
                T[j]=ans
    print('#%i'%t,ans)