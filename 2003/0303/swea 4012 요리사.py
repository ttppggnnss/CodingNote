import sys
sys.stdin=open('input.txt','r')

from itertools import combinations as c
u=input;r=range
def f(i):x,y=i;return S[x][y]+S[y][x]
for t in r(1,1+int(u())):
    n=int(u());ans=9**9;S=[[*map(int,u().split())] for _ in'a'*n]
    for i in c(r(n),n//2):
        # print(sum(map(f,c(i,2))), sum(map(f,c({*r(n)}-{*i},2))))
        res=abs(sum(map(f,c(i,2)))-sum(map(f,c({*r(n)}-{*i},2))))
        if res<ans:ans=res
        if ans==0:break
    print('#%i'%t,ans)
