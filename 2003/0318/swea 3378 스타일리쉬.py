# 틀림
import sys
sys.stdin=open('input.txt','r')
from itertools import product as pr
for t in range(1,int(input())+1):
    p,q=map(int,input().split())
    a=b=c=d=e=f=0
    data1=[[0,0,0]] # () {} [] 개수
    data2=[] # . 개수
    data3=[] # 가능한 R,C,S
    for _ in'a'*p:
        s=input()
        s2=s.lstrip('.')
        dot=len(s)-len(s2)
        for i in s:
            if i=='(':a+=1
            if i==')':a-=1
            if i=='{':b+=1
            if i=='}':b-=1
            if i=='[':c+=1
            if i==']':c-=1
        data1.append([a,b,c])
        data2.append(dot)
    for j in pr(range(1,21),repeat=3):
        x,y,z=j # 가능한 R,C,S
        for i in range(1,p):
            if x*data1[i][0]+y*data1[i][1]+z*data1[i][2]!=data2[i]:
                break
        else:data3.append([x,y,z])
    R=set();C=set();S=set()
    for i in data3:
        R.add(i[0])
        C.add(i[1])
        S.add(i[2])
    if len(R)==1:
        R=R.pop()
    if len(C)==1:
        C=C.pop()
    if len(S)==1:
        S=S.pop()
    dots = [0]
    for _ in'a'*(q-1):
        s3=input()
        for i in s3:
            if i == '(': d += 1
            if i == ')': d -= 1
            if i == '{': e += 1
            if i == '}': e -= 1
            if i == '[': f += 1
            if i == ']': f -= 1
        if d==0:R2=0
        elif type(R)==int:R2=R*d
        else:R2=None
        if e==0:C2=0
        elif type(C)==int:C2=C*e
        else:C2=None
        if f==0:S2=0
        elif type(S)==int:S2=S*f
        else:S2=None
        if R2==None and C2==None and d==e:
            A=set()
            for i in data3:
                A.add(i[0]+i[1])
            if len(A)==1:RC2=A.pop()*d
            else:RC2=None
        if R2==None and S2==None and d==f:
            A=set()
            for i in data3:
                A.add(i[0]+i[2])
            if len(A)==1:RS2=A.pop()*d
            else:RS2=None
        if C2==None and S2==None and e==f:
            A=set()
            for i in data3:
                A.add(i[1]+i[2])
            if len(A)==1:CS2=A.pop()*e
            else:CS2=None
        if R2==None and C2==None and S2==None and d==e and e==f:
            for i in data3:
                A.add(i[0]+i[1]+i[2])
            if len(A)==1:RCS2=A.pop()*d
            else:RCS2=None
        try:
            dots.append(R2+C2+S2)
        except:
            try:
                dots.append(RC2+S2)
            except:
                try:
                    dots.append(RS2+C2)
                except:
                    try:
                        dots.append(CS2+R2)
                    except:
                        try:
                            dots.append(RCS2)
                        except:
                            dots.append(-1)
    input()
    print('#%i'%t,*dots)