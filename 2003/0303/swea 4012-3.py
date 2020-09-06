import sys
sys.stdin=open('input.txt','r')

from itertools import combinations as c
u=input;r=range
for t in r(1,1+int(u())):
    n=int(u())
    ans=9**9
    L=[[*map(int,u().split())]for _ in'a'*n]
    # M 에서 i, j 는 각각 1부터 n번째 가로줄, 세로줄
    M=[sum(i)+sum(j) for i,j in zip(L,zip(*L))]
    S=sum(M)//2 # L에 있는 것들 모두 합한 값
    for i in c(M,n//2):# sum(i) 는 절반 선택해서 합한 것을 두배 한 것
        ans=min(ans,abs(S-sum(i))) # 구하려는 것 : 반쪽 합 - 나머지 합 => 에다가 양쪽다 나머지 합을 더한 것 : 전체 - 2*나머지 합
    print('#%i'%t,ans)
