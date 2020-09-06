# 황수현 풀이 참고 그런데 느림
import sys
sys.stdin=open('input.txt','r')

for t in range(int(input())):
    input();mx=-9**9;mn=9**9;a,b,c,d=map(int,input().split());N=[*map(int,input().split())];q=[[N[0],a,b,c,d,1]]
    while q:
        p=q.pop()
        if p[5]==len(N):mx=max(p[0],mx);mn=min(p[0],mn)
        else:
            for j in range(1,5):
                if p[j]>0:
                    if p[1]>0 and j==1:
                        q.append([p[0]+N[p[5]],p[1]-1,p[2],p[3],p[4],p[5]+1])
                    elif p[2]>0 and j==2:
                        q.append([p[0]-N[p[5]],p[1],p[2]-1,p[3],p[4],p[5]+1])
                    elif p[3]>0 and j==3:
                        q.append([p[0]*N[p[5]],p[1],p[2],p[3]-1,p[4],p[5]+1])
                    else:q.append([int(p[0]/N[p[5]]),p[1],p[2],p[3],p[4]-1,p[5]+1])
    print("#%d %d" % (t+1,mx-mn))