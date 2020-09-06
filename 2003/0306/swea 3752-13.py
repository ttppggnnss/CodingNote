# idea 2
T=int(input())
for tc in range(1,T+1):
    N = int(input())
    p = list(map(int, input().split()))
    ans=[0]
    for x in p:
        num=[]
        for y in ans:
            num.append(x+y)
        ans+=num
    print('#{} {}'.format(tc, len(set(ans))))

# idea 3
T=int(input())
for tc in range(1, T+1):
    n=int(input())
    p=list(map(int,input().split()))
    ans=set([0])
    for x in p:
        num=set()
        for y in ans:
            num.add(x+y)
        ans = set(list(ans)+list(num))
    print('#{} {}'.format(tc,len(set(ans))))

# idea 4
T = int(input())
for tc in range(1,T+1):
    n=int(input())
    p=list(map(int,input().split()))
    total=sum(p)
    s=[0]*(total+1)
    s[0]=1
    for x in p:
        for i in range(total-x,-1,-1):
            if s[i]==1:
                s[i+x]=1
    print('#{} {}'.format(tc, sum(s)))

# idea 4-2
T = int(input())
for tc in range(1,T+1):
    n=int(input())
    p=list(map(int,input().split()))
    total=sum(p)
    s=[0]*(total+1)
    s[0]=1
    for x in p:
        for i in range(total-x,-1,-1):
            s[i+x]|=s[i]
    print('#{} {}'.format(tc, sum(s)))
