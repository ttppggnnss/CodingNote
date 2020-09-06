import sys
sys.stdin=open('input.txt','r')

for t in range(1, int(input())+1):
    b=[[*map(int,input().split())]for _ in'a'*9]
    b+=[list(i) for i in zip(*b)]
    for i in range(3):
        for j in range(3):
            b+=[b[i*3][j*3:j*3+3]+b[i*3+1][j*3:j*3+3]+b[i*3+2][j*3:j*3+3]]
    ans=1
    for i in b:
        if set(i)!={1,2,3,4,5,6,7,8,9}:ans=0
    print('#%i'%t,ans)