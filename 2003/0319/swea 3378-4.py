import sys
sys.stdin=open('../input.txt','r')

from itertools import product

for t in range(1,int(input())+1):
    # 기본 입력
    p,q = map(int,input().split())
    Master = [input() for _ in 'a'*p]
    Me = [input() for _ in 'a'*q]

    # Master . 갯수, (){}[] 갯수
    a=b=c=0
    Master_dot=[]
    Master_bracket=[[0,0,0]]
    for i1 in Master:
        Master_dot.append(len(i1)-len(i1.lstrip('.')))
        for j1 in i1:
            if j1=='(':a+=1
            if j1==')':a-=1
            if j1=='{':b+=1
            if j1=='}':b-=1
            if j1=='[':c+=1
            if j1==']':c-=1
        Master_bracket.append([a,b,c])

    # R,C,S 가능성 있는 것들
    candidate=[]

    # 가능한 모든 R,C,S
    for i2 in product(range(1,21), repeat=3):
        R1,C1,S1=i2
        for j2 in range(1,p):
            a1,b1,c1=Master_bracket[j2]
            if R1*a1+C1*b1+S1*c1!=Master_dot[j2]:
                break
        else:
            candidate.append([R1,C1,S1])

    # Me (){}[] 갯수
    d=e=f=0
    Me_bracket=[]
    for i3 in Me:
        for j3 in i3:
            if j3=='(':d+=1
            if j3==')':d-=1
            if j3=='{':e+=1
            if j3=='}':e-=1
            if j3=='[':f+=1
            if j3==']':f-=1
        Me_bracket.append([d,e,f])

    # 가능성 있는 것들에 대해서 나올 수 있는 점들
    Me_dot=[set() for _ in'a'*q]
    for i4 in range(q):
        d1,e1,f1=Me_bracket[i4]

        for j4 in candidate:
            R2,C2,S2=j4
            Me_dot[i4].add(R2*d1+C2*e1+S2*f1)
        if candidate==[]:
            Me_dot[i4]=-1
        elif len(Me_dot[i4])==1:
            Me_dot[i4]=Me_dot[i4].pop()
        else:
            Me_dot[i4]=-1

    # Me_dot 중 마지막 갯수는 필요 없다
    # 처음에는 0 이 온다
    Me_dot=[0]+Me_dot[:-1]
    print('#%i'%t,*Me_dot)




