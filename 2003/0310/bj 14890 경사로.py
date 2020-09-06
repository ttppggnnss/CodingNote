# 맞췄는데 더럽다
import sys
sys.stdin=open('input.txt','r')

def f(i,l,v):
    s=[i[0]]
    for j in range(n-1):
        if len(s)<=j:break
        if i[j+1]==s[j]:
            s.append(i[j+1])
        elif i[j+1]==s[j]+1:
            if j>=l-1:
                z=1
                for k in range(1,l+1):
                    s[-k]+=1
                    if v[j+1-k]<1:
                        v[j+1-k]=1
                    else:z=0;break
                if z:
                    if i[j+1]==s[j]:
                        s.append(i[j+1])
        elif i[j+1]==s[j]-1:
            if j+l<n:
                z=1
                for k in range(1,l+1):
                    if i[j+1]==i[j+k]:
                        if v[j+k]<1:
                            v[j+k]=1
                        else:z=0;break
                    else:z=0;break
                if z:
                    s[j]-=1
                if i[j+1]==s[j]:
                    s.append(i[j+1])
                else:break
        else:break
    if len(s)==n:return 1
    else:return 0

n,l=map(int,input().split())
b=[[*map(int,input().split())]for _ in'a'*n]
b+=[list(i) for i in zip(*b)]
ans=0
for i in b:
    v=[0]*n
    ans+=f(i,l,v)
print(ans)