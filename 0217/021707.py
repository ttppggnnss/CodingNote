import sys
sys.stdin=open("input021707.txt","r")

def backtrack(L,L1,L2,L3,L4):
    if sum(L3)<=L:
        global score
        score=max(score,sum(L4))
    if sum(L3)>L:
        return
    for k,v in enumerate(L2):
        L2.remove(v)
        L3.append(v)
        a=L1[k]
        L4.append(a)
        L1.remove(a)
        backtrack(L,L1[k:],L2[k:],L3,L4)
        L3.pop()
        L4.pop()
        L2.insert(k,v)
        L1.insert(k,a)

for t in range(1,int(input())+1):
    N, L = map(int,input().split())
    L1=[]
    L2=[]
    L3=[]
    L4=[]
    for i in range(N):
        a,b=map(int,input().split())
        L1.append(a) # 점수
        L2.append(b) # 칼로리
    score=0
    backtrack(L,L1,L2,L3,L4)
    print("#%i"%t,score)