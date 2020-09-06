import sys
sys.stdin=open('input.txt','r')

for t in range(1,int(input())+1):
    n, m = map(int,input().split())
    ci=list(enumerate([*map(int,input().split())],1))
    ci=[list(i) for i in ci]
    ci2=[[0,0]]*n
    time=0
    ans=0
    while time+1:
        for i in range(n):
            if time%n==i:
                if ci2[i][1]==0 and ci!=[]:
                    ci2[i]=ci.pop(0)
                else:
                    ci2[i][1]=ci2[i][1]//2
                    if ci2[i][1]==0 and ci!=[]:
                        ci2[i]=ci.pop(0)
                time+=1
            if ci == []:
                cnt = 0
                for i in range(n):
                    if ci2[i][1] == 0:
                        cnt += 1
                if cnt == n - 1:
                    for i in range(n):
                        if ci2[i][1] == 1:
                            ans = ci2[i][0]
                        if ans: break
                    if ans: break
            if ans:break
        if ans: break
    print('#%i'%t,ans)