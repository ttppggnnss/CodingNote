import sys
sys.stdin=open('../input.txt','r')

from itertools import product
def func(i,a,b,c):
    for j in i:
        if j=='(':a+=1
        if j==')':a-=1
        if j=='{':b+=1
        if j=='}':b-=1
        if j=='[':c+=1
        if j==']':c-=1
    return a,b,c
for t in range(1,int(input())+1):
    p,q=map(int,input().split());M1=[input() for _ in 'a'*p];M2=[input() for _ in 'a'*q];M1d=[];M1b=[[0,0,0]];a=b=c=d=e=f=0
    for i1 in M1:M1d.append(len(i1)-len(i1.lstrip('.')));a,b,c=func(i1,a,b,c);M1b.append([a,b,c])
    ca=[]
    for i2 in product(range(1,21), repeat=3):
        R1,C1,S1=i2
        for j2 in range(1,p):
            a1,b1,c1=M1b[j2]
            if R1*a1+C1*b1+S1*c1!=M1d[j2]:break
        else:ca.append([R1,C1,S1])
    M2b=[]
    for i3 in M2:d,e,f=func(i3,d,e,f);M2b.append([d,e,f])
    M2d=[set() for _ in'a'*q]
    for i4 in range(q):
        d1,e1,f1=M2b[i4]
        for j4 in ca:R2,C2,S2=j4;M2d[i4].add(R2*d1+C2*e1+S2*f1)
        if ca==[]:M2d[i4]=-1
        elif len(M2d[i4])==1:M2d[i4]=M2d[i4].pop()
        else:M2d[i4]=-1
    M2d=[0]+M2d[:-1]
    print('#%i'%t,*M2d)




