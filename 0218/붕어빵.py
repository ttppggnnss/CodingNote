import sys
sys.stdin=open('붕어빵.txt','r')

for t in range(1,int(input())+1):
    n,m,k=map(int,input().split());nums=list(map(int,input().split()));s=1;c=0;a='Possible'
    if 0 in nums:a='Impossible'
    else:
        while s<max(nums)+1:
            if s%m==0:c+=k
            if s in nums:c-=nums.count(s)
            if c<0:a='Impossible';break
            s+=1
    print('#%d'%t,a)