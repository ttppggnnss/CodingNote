# 숏코딩
import sys
sys.stdin=open('input.txt','r')

for T in range(1,11):
    L,S=map(int,input().split());C=list(map(int,input().split()));R=[[]for i in range(101)];Q=[[S]];V=[S]
    for i in range(L//2):R[C[2*i]]+=[C[2*i+1]]
    while Q[-1]:
        Q+=[[]]
        for i in Q[-2]:
             for j in R[i]:
                   if j not in V:Q[-1]+=[j];V+=[j]
    print("#%d %d"%(T,max(Q[-2])))