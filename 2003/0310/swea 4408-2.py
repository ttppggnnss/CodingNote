for t in range(1,int(input())+1):
    s=[0]*201
    for _ in'a'*int(input()):
        a,b=map(int,input().split());a=(a+1)//2;b=(b+1)//2
        if a>b:a,b=b,a
        for i in range(a,b+1):s[i]+=1
    print('#%i' % t, max(s))