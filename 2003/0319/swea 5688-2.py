import sys
sys.stdin=open('../input.txt','r')

Data=[i**3 for i in range(10**6)]
for t in range(1,int(input())+1):
    try:print('#%i'%t,Data.index(int,input()))
    except:print('#%i'%t,-1)
