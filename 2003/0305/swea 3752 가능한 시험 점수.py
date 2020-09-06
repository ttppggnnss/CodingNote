# 시간 초과
import sys
sys.stdin=open('input.txt','r')

def bt(now,score):
    global ans
    for k,v in enumerate(score):
        now+=v
        ans.add(now)
        if len(score)>1:
            bt(now,score[k+1:])
        now-=v
for t in range(1,1+int(input())):
    n=int(input())
    score=[*map(int,input().split())]
    ans={0}
    bt(0,score)
    print('#%i'%t,len(ans))
