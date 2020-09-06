# 황수현 풀이 참고
import sys
sys.stdin=open('input.txt','r')

for t in range(int(input())):
    input()
    mx=-100000001
    mn=100000001
    op=[*map(int,input().split())]
    N=[*map(int,input().split())]
    q=[[N[0],op,1]]*4
    while q:
        tmp=q.pop()
        if tmp[2]==len(N):
            mx=max(tmp[0],mx)
            mn=min(tmp[0],mn)
        else:
            for j in range(4):
                if tmp[1][j]>0:
                    if j==0:
                        q.append([tmp[0]+N[tmp[2]],[tmp[1][0]-1]+tmp[1][1:],tmp[2]+1])
                    elif j==1:
                        q.append([tmp[0]-N[tmp[2]],[tmp[1][0]]+[tmp[1][1]-1]+tmp[1][2:],tmp[2]+1])
                    elif j==2:
                        q.append([tmp[0]*N[tmp[2]],tmp[1][:2]+[tmp[1][2]-1]+[tmp[1][3]],tmp[2]+1])
                    else:
                        q.append([int(tmp[0]/N[tmp[2]]),tmp[1][:3]+[tmp[1][3]-1],tmp[2]+1])
    print("#%d %d" % (t+1,mx-mn))