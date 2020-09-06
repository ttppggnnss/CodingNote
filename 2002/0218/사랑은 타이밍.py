import sys
sys.stdin=open("사랑은 타이밍.txt","r")

for t in range(1,int(input())+1):
    a1,b1,c1=11,11,11
    a,b,c=map(int,input().split())
    ans=(a-a1-1)*60*24 + (b+24-b1-1)*60 +c+60-c1
    if ans<0:ans=-1
    print('#%d'%t,ans)