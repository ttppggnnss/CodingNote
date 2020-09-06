import sys
sys.stdin=open('input.txt','r')

for t in range(1,int(input())+1):
    a, b, c, d=map(int,input().split())
    plan=[*map(int,input().split())]
    ans=0
    i=0
    while i<12:
        if i<=9 and plan[i] and plan[i+1] and plan[i+2]:
            ans1=0
            for j in range(i,i+3):
                if b>a*plan[j]:
                    ans1+=a*plan[j]
                else:
                    ans1+=b
            if c>ans1:
                ans+=ans1
            else:
                ans+=c
            i+=3
        elif i==10 and plan[i] and plan[i+1]:
            ans1=0
            for j in range(i,i+2):
                if b>a*plan[j]:
                    ans1+=a*plan[j]
                else:
                    ans1+=b
            if c>ans1:
                ans+=ans1
            else:
                ans+=c
            i+=3
        else:
            if b>a*plan[i] and c>a*plan[i]:
                ans+=a*plan[i]
                i+=1
            elif b<c:
                ans+=b
                i+=1
            else:
                ans+=c
                i+=3
    ans=min(ans,d)
    print('#%i'%t,ans)