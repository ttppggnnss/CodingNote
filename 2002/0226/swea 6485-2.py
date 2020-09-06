import sys
sys.stdin=open('input.txt','r')

for t in range(1, int(input())+1):
    b=[[*map(int,input().split())] for _ in [0]*int(input())];s=[]
    for i in range(int(input())):c=int(input());s.append(sum(1 for j in b if j[0]<=c<=j[1]))
    print('#%i'%t,*s)