import sys
sys.stdin=open('../input.txt','r')

n=int(input().strip())
ch=input().strip()
x,y=map(int,input().strip().split())

tree=[0]*(n+1)
tree2=[]
tree3=[0]*1000
a=b=0
s1=1
z=[]
for i in range(2*n):
    if ch[i]=='0':
        a+=1
        if tree[s1]==0:
            tree[s1]=a
            tree3[i]=a
        else:
            s1+=1
            tree[s1]=a
            tree3[i]=a
        s1=2*s1
        if i==x-1 or i==y-1:
            z.append(a)
    else:
        s1=s1//2
        b=a
        if b not in tree2:
            tree2.append(b)
            tree3[i]=b
        else:
            while b in tree2:
                b-=1
            tree2.append(b)
            tree3[i]=b
        if i==x-1 or i==y-1:
            z.append(b)
z=sorted([tree.index(i) for i in z])
z1=[]
z2=[]
c=z[0]
d=z[1]
while c>0:
    z1.append(c)
    c//=2
while d>0:
    z2.append(d)
    d//=2
croot=0
for i in z1:
    for j in z2:
        if i==j:
            croot=i
            break
    if croot:
        break
ans1=tree3.index(croot)+1
ans2=10-(tree3[::-1].index(croot))
print(ans1,ans2)
