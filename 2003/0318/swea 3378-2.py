# 틀림
import sys
sys.stdin=open('input.txt','r')

from itertools import product as pr

for t in range(1,int(input())+1):
    p,q=map(int,input().split())
    a=b=c=d=e=f=0
    data=[]
    abc=[[0,0,0]]
    dot_num=[]

    for _ in'a'*p:
        s=input()
        s2=s.lstrip('.')
        dot_num.append(len(s)-len(s2))
        for i in s:
            if i=='(':a+=1
            if i==')':a-=1
            if i=='{':b+=1
            if i=='}':b-=1
            if i=='[':c+=1
            if i==']':c-=1
        abc.append([a,b,c])

    R=[];C=[];S=[]
    for j in pr(range(1,21),repeat=3):
        x,y,z=j # 가능한 R,C,S
        for i in range(1,p):
            if x*abc[i][0]+y*abc[i][1]+z*abc[i][2]!=dot_num[i]:
                break
        else:R.append(x);C.append(y);S.append(z)

    k=len(R)
    if len(set(R))==1:R=R[0]
    if len(set(C))==1:C=C[0]
    if len(set(S))==1:S=S[0]
    ans=[0]

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
            for i in range(k):
                A.add(R[i]+C[i])
            if len(A)==1:RC2=A.pop()*d
            else:RC2=None
        if R2==None and S2==None and d==f:
            A=set()
            for i in range(k):
                A.add(R[i]+S[i])
            if len(A)==1:RS2=A.pop()*d
            else:RS2=None
        if C2==None and S2==None and e==f:
            A=set()
            for i in range(k):
                A.add(C[i]+S[i])
            if len(A)==1:CS2=A.pop()*e
            else:CS2=None
        if R2==None and C2==None and S2==None and d==e and e==f:
            for i in range(k):
                A.add(R[i]+C[i]+S[i])
            if len(A)==1:RCS2=A.pop()*d
            else:RCS2=None
        try:
            ans.append(R2+C2+S2)
        except:
            try:
                ans.append(RC2+S2)
            except:
                try:
                    ans.append(RS2+C2)
                except:
                    try:
                        ans.append(CS2+R2)
                    except:
                        try:
                            ans.append(RCS2)
                        except:
                            ans.append(-1)
    input()
    print('#%i'%t,*ans)