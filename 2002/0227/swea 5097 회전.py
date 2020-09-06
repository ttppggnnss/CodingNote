import sys
sys.stdin=open('input.txt','r')

for t in range(1,int(input())+1):
    n,m=map(int,input().split())
    m=m%n
    L=[*input().split()]
    print('#%i'%t,L[m])