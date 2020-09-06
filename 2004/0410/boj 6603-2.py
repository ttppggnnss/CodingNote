import sys
sys.stdin=open('../input.txt','r')

def c(s,n,visit,k=0,p=[]):
    if k==6:
        print(*p)
        return
    for i in range(len(s)):
        if visit[i]<1:
            p.append(s[i])
            visit[i]=1
            if i<len(s):
                c(s[i+1:],n,visit[i+1:],k+1,p[:])
            else:
                if k==5:
                    print(*p)
                    return
                else:
                    return
            visit[i]=0
            p.pop()

while 1:
    s=[*map(int,input().split())]
    n=s.pop(0)
    if n==0: break
    visit=[0]*n
    c(s,n,visit,0,[])
    print()