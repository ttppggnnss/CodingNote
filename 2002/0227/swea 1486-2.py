import sys
sys.stdin=open('input.txt','r')

for T in range(int(input())):
    N,B=map(int,input().split())
    M=list(map(int,input().split()))
    temp=[]
    r=9**9
    for i in M:
        for j in range(len(temp)):
            a=i+temp[j]
            if a>=B and a<r:r=a
            if a<B:temp+=[a]
        temp=list(set(temp+[i]))
        if r==B:break
    print("#%d %d"%(T+1,r-B))