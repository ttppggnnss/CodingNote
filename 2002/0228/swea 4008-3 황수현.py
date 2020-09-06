# 황수현 풀이
import sys
sys.stdin=open('input.txt','r')

for t in range(1,1+int(input())):
    input()
    ans=[-100000001,100000001]
    giho=list(map(int,input().split()))
    numbers = list(map(int, input().split()))
    q=[]
    for i in range(4):
        if giho[i]!=0:
            if i ==0:
                q.append([numbers[0] + numbers[1], [giho[0]-1] + giho[1:],2])
            elif i == 1:
                q.append([numbers[0] - numbers[1], [giho[0]]+[giho[1]-1] + giho[2:],2])
            elif i == 2:
                q.append([numbers[0] * numbers[1], giho[0:2]+[giho[2]-1] + [giho[3]],2])
            else:
                q.append([numbers[0]//numbers[1],giho[:3]+[giho[3]-1],2])
    while q:
        tmp=q.pop()
        if tmp[2]==len(numbers):
            if tmp[0]>ans[0]:
                ans[0]=tmp[0]
            if tmp[0]<ans[1]:
            	ans[1]=tmp[0]
        else:
            for i in range(4):
                if tmp[1][i] > 0:
                    if i == 0:
                        q.append([tmp[0] + numbers[tmp[2]], [tmp[1][0] - 1] + tmp[1][1:],tmp[2]+1])
                    elif i == 1:
                        q.append([tmp[0] - numbers[tmp[2]], [tmp[1][0]] + [tmp[1][1] - 1] + tmp[1][2:],tmp[2]+1])
                    elif i == 2:
                        q.append([tmp[0] * numbers[tmp[2]], tmp[1][0:2] + [tmp[1][2] - 1] + [tmp[1][3]],tmp[2]+1])
                    else:
                        q.append([int(tmp[0] / numbers[tmp[2]]), tmp[1][:3] + [tmp[1][3] - 1],tmp[2]+1])
    print("#%d %d"%(t,ans[0]-ans[1]))