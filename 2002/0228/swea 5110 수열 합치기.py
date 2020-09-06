# 시간초과
import sys
sys.stdin=open('input.txt','r')

for t in range(1,int(input())+1):
    n,m=map(int,input().split())
    L=[*map(int,input().split())]
    for i in 'a'*(m-1):
        a=len(L)
        L2=[*map(int,input().split())]
        for i in range(1,max(L)):
            try:
                c=L.index(L2[0]+i)
                L=L[:c]+L2+L[c:]
                break
            except:
                pass
        if len(L)==a:
            L=L+L2
    print('#%i'%t,*L[::-1][:10])