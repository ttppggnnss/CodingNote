import sys
sys.stdin=open('input.txt','r')

def g(i,j,b):
    a=b[i][j]
    b[i][j]=0
    for k in range(a):
        if -1<i+k<h:g(i+k,j,b)
        if -1<j+k<w:g(i,j+k,b)
        if -1<i-k<h:g(i-k,j,b)
        if -1<j-k<w:g(i,j-k,b)

def f(k,b):
    if k==0:
        global ans
        s = w * h
        for i in b:
            s -= i.count(0)
        ans=min(ans,s)
        return
    for i in range(w):
        b2 = [[i for i in j] for j in b]
        for j in range(h):
            if b[j][i]>0:
                g(j,i,b2)
                for c in range(w):
                    for d in range(h - 1, 0, -1):
                        if b2[d][c] < 1:
                            for e in range(d - 1, -1, -1):
                                if b2[e][c] > 0:
                                    b2[d][c], b2[e][c] = b2[e][c], b2[d][c]
                                    break
                f(k-1,b2)
                break
    else:
        f(k-1,b2)
for t in range(1,1+int(input())):
    n,w,h=map(int,input().split());ans=9**9
    b=[[*map(int,input().split())]for _ in'a'*h]
    f(n,b)
    print('#%i'%t,ans)