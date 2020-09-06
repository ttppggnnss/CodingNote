import sys
sys.stdin=open('input.txt','r')

for t in range(1,int(input())+1):
    n,m,l=map(int,input().split())
    L=[*map(int,input().split())]
    for i in 'a'*m:
        a,b=map(int,input().split())
        L.insert(a,b)
    print('#%i'%t,L[l])