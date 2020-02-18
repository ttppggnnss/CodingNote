import sys
sys.stdin=open("input021707.txt","r")

def HBG(S1,K1,start,end):
    global sum_S,sum_K,score,L
    if sum_K>L:
        return
    if sum_K<=L:
        score=max(sum_S,score)
    if start<end:
        sum_S+=S1[start]
        sum_K+=K1[start]
        HBG(S1,K1,start+1,end)
        sum_S-=S1[start]
        sum_K-=K1[start]
        HBG(S1,K1,start+1,end)

for t in range(1, int(input()) + 1):
    N, L = map(int, input().split())
    sum_S=sum_K=score=0
    S1=[];K1=[]
    for i in range(N):
        S,K = map(int, input().split())
        S1.append(S);K1.append(K)
    HBG(S1,K1,0,N)
    print('#{} {}'.format(t, score))