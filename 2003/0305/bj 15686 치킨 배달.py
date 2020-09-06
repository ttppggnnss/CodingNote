import sys
sys.stdin=open('input.txt','r')
input=sys.stdin.readline

from itertools import combinations as c

def f(h,z,ans=9**9): # ans는 최대값으로 초기화
    i,j=h
    for k in z:
        d,e=k
        ans=min(ans,abs(i-d)+abs(j-e))
    return ans # 치킨집들 중 최소 치킨거리 반환

u=input
n,m=map(int,u().split())
b=[] # 지도
H=[] # 집 좌표
C=[] # 치킨 집 좌표
for i in range(n):
    b+=[[*map(int,u().split())]]
    for j in range(n):
        if b[-1][j]==1:
            H.append((i,j))
        elif b[-1][j]==2:
            C.append((i,j))
ans=9**9
for i in c(C,m): # 치킨 집 좌표 중 m개 선택한 것들 마다 계산
    res=0
    for j in H: # 집 좌표마다
        res+=f(j,i) # 최소 치킨거리 더한다
    ans=min(res,ans) # 도시 치킨거리 값들 중 최솟값
print(ans)