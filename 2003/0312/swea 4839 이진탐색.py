def bin(l,r,p):
    cnt=0
    while l<=r:
        c=(l+r)>>1
        cnt+=1
        if c==p:break
        elif c>p:r=c
        else:l=c
    return cnt

for t in range(1,int(input())+1):
    r,p1,p2=map(int, input().split())
    if bin(1,r,p1)>bin(1,r,p2):ans='B'
    elif bin(1,r,p1)<bin(1,r,p2):ans='A'
    else:ans=0
    print('#%i'%t,ans)