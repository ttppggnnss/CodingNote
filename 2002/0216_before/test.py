import sys;sys.stdin=open("input.txt","r")
# 여자 친구 만나러 가는 데 드는 최소 비용
# 갈 수 없다면 "-1" 준혁이는 1, 여자친구는 7
# 최소비용 경로

# 정리
v,e = map(int,input().split()) # vortex, edge

MyMap=[[0]*(v+1) for _ in[0]*(v+1)]

for _ in [0]*e:
    v1,v2,cost=map(int,input().split())
    MyMap[v2][v1]=cost

ans=[]
ans2=[]
history=[]

def bf(v2,res,history):
    if v2==v:
        global ans,ans2
        ans.append(res)
        ans2.append(history[:]+[v])
        return

    for i in range(1,v+1):
        if MyMap[i][v2]!=0:
            res+=MyMap[i][v2]
            constant=MyMap[i][v2]
            history.append(v2)
            MyMap[i][v2] = 0
            bf(i,res,history)
            MyMap[i][v2] = constant
            history.pop()
            res-=constant

bf(1,0,history)

if ans==[]:
    print(-1)
else:
    print(min(ans))
    print(ans2[ans.index(min(ans))])