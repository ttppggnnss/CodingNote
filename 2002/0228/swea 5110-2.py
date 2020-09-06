# 10개 중 9개 통과 시간초과 
import sys
sys.stdin=open('input.txt','r')

def f(a):
    if max(L)>a:
        for i in L:
            if i>a:
                return L.index(i)
    else:
        return -1

for t in range(1,int(input())+1):
    n,m=map(int,input().split())
    L=[*map(int,input().split())]
    for i in 'a'*(m-1):
        L2=[*map(int,input().split())]
        a=f(L2[0])
        if a<0:
            L=L+L2
        else:
            L=L[:a]+L2+L[a:]
    print('#%i'%t,*L[::-1][:10])