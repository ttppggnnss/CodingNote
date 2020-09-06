import sys
sys.stdin=open('input.txt','r')

from itertools import combinations as c
def f(i):x,y=i;return b[x][y]+b[y][x]
n=int(input());ans=9**9
b=[[*map(input().split())]for _ in'a'*n]
for i in c(range(n),n//2):
    res=abs(sum(map(f,c(i,2)))-sum(map(f,c({*range(n)}-{*i},2))))
    if res<ans:ans=res
    if ans==0:break
print(ans)