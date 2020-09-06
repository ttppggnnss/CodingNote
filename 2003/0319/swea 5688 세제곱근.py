import sys
sys.stdin=open('../input.txt','r')

for t in range(1,int(input())+1):
    a=round(pow(int(input()),1/3),2)
    if a!=int(a):a=-1
    print('#%i'%t,int(a))
