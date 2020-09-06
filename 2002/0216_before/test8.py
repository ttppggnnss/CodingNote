n=int(input())
def q(pst,y):
    global ans
    if y==n:
        ans+=1
        return
    for i in range(n):
        k=1
        for j in range(y):
            if pst[j]==i or abs(pst[j]-i)==abs(y-j):
                k=0
                break
        if k:
            q(pst+[i],y+1)
ans=0
q([],0)
print(ans)