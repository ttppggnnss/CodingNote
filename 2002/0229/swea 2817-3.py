# 수정 본 실행시간 반으로 줄어듬
def bt(k,L,L2,suma):
    global cnt
    for id,x in enumerate(L):
        suma+=x
        if suma>k:
            suma-=x
            continue
        if suma<k:
            L4=L[id+1:]
            bt(k,L4,L2,suma)
        if suma==k:
            cnt+=1
        suma-=x
for t in range(1,int(input())+1):
    n, k = map(int,input().split())
    L=[*map(int,input().split())]
    cnt=0
    bt(k,L,[],0)
    print("#%i"%t, cnt)