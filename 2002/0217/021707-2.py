import sys
sys.stdin=open("input021707.txt","r")

def ham(sco,kal,scosum,kalsum,L):
    print(kalsum)
    print(scosum)
    if kalsum<=L:
        global score
        if score<scosum:
            score=scosum
            return
    if scosum>L:
        return
    for i, v in enumerate(kal):
        kalsum+=v
        kal.remove(v)
        a=sco[i]
        scosum+=a
        sco.remove(a)
        ham(sco[i:],kal[i:],scosum,kalsum,L)
        kalsum-=v
        scosum-=a
        kal.insert(i,v)
        sco.insert(i,a)


for t in range(1, int(input())+1):
    N, L = map(int,input().split())
    sco=[]
    kal=[]
    for i in range(N):
        s, k = map(int,input().split())
        sco.append(s)
        kal.append(k)
    scosum=0
    kalsum=0
    score=0
    ham(sco,kal,scosum,kalsum,L)
    print("#%i"%t,score)
