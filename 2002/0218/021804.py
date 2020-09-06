# 토너먼트 카드 게임

import sys
sys.stdin=open("input4.txt","r")

def rsp(L,M):
    # group 1
    L1=L[:(len(L)-1)//2+1]
    M1=M[:(len(M)-1)//2+1]
    # group 2
    L2=L[(len(L)-1)//2+1:]
    M2=M[(len(M)-1)//2+1:]

    # ans1
    if len(L1)==1:ans1=L1[0],M1[0]
    if len(L1)==2:
        if (L1[1]-L1[0])%3==1:ans1=L1[1],M1[1]
        else:ans1=L1[0],M1[0]
    if len(L1)>2:ans1=rsp(L1,M1)
    # ans2
    if len(L2)==1:ans2=L2[0],M2[0]
    if len(L2)==2:
        if (L2[1]-L2[0])%3==1:ans2=L2[1],M2[1]
        else:ans2=L2[0],M2[0]
    if len(L2)>2:ans2=rsp(L2,M2)

    # ans
    if (ans2[0]-ans1[0])%3==1:return ans2
    else:return ans1

for t in range(1,int(input())+1):
    input()
    L=list(map(int,input().split()))
    M=list(range(1,len(L)+1))
    print('#%i'%t,rsp(L,M)[1])