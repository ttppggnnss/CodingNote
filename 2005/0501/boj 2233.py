# 런타임 에러
import sys
sys.stdin=open('../input.txt','r')

n=int(input())
n2=[*map(int,input())]

tree=[0]*(n+1)
tree2=[]
s=1
a=0
for i in n2:
    if i==0:
        if tree[s]!=0:
            s+=1
        a+=1
        tree[s]=a
        s=2*s
    else:
        b=a
        if b not in tree2:
            tree2.append(b)
        else:
            while b in tree2:
                b-=1
            tree2.append(b)
        s=s//2
i,j=map(int,input().split())
if n2[i-1]==0:
    i2=n2[:i].count(0)
else:
    i2=n2[:i].count(0)+1-n2[:i+1].count(1)
if n2[j-1]==0:
    j2=n2[:j].count(0)
else:
    j2=n2[:j].count(0)+1-n2[:j+1].count(1)

i2=tree.index(i2)
j2=tree.index(j2)


if j2<i2:
    i2,j2=j2,i2
j3=j2
while j3!=i2 and j3>0:
    j3=j3//2

if j3>0:
    ans=tree.index(i2)
else:
    ans=min(i2,j2)//2

ans2=tree2.index(ans)+1
ans3=[]
a=b=0
for i in range(2*n):
    if n2[i]==0:
        a+=1
        if a==ans:
            ans3.append(i+1)
    else:
        b+=1
        if b==ans2:
            ans3.append(i+1)
print(*ans3)