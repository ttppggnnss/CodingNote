# 황수현 풀이 참고
import sys
sys.stdin=open('input.txt','r')

for t in range(int(input())):
    input()
    mx=-9**9
    mn=9**9
    a,b,c,d=map(int,input().split())
    N=[*map(int,input().split())]
    q=[[N[0],a,b,c,d,1]]*4
    while q:
        tmp=q.pop()
        m=tmp[0]
        a=tmp[1]
        b=tmp[2]
        c=tmp[3]
        d=tmp[4]
        i=tmp[5]
        if i==len(N):
            mx=max(m,mx)
            mn=min(m,mn)
        else:
            for j in range(1,5):
                if tmp[j]>0:
                    if a>0 and j==1:
                        q.append([m+N[i],a-1,b,c,d,i+1])
                    elif b>0 and j==2:
                        q.append([m-N[i],a,b-1,c,d,i+1])
                    elif c>0 and j==3:
                        q.append([m*N[i],a,b,c-1,d,i+1])
                    elif d>0 and j==4:
                        q.append([int(m/N[i]),a,b,c,d-1,i+1])
    print("#%d %d" % (t+1,mx-mn))