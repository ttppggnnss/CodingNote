import sys
sys.stdin=open('input.txt','r')

for t in range(1,11):
    v,s=map(int,input().split());L=[*map(int,input().split())];V=[set()for i in 'a'*v];q=[[s]];p=[0]*v;p[s]=1
    for i in range(len(L)//2):V[L[2*i]].add(L[2*i+1])
    while q[-1]:
        q+=[[]]
        for i in q[-2]:
            for j in V[i]:
                if not p[j]:q[-1]+=[j];p[j]=1
    print("#%d"%t,max(q[-2]))