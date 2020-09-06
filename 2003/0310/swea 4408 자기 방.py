import sys
sys.stdin=open('input.txt','r')

for t in range(1,int(input())+1):
    n=int(input())
    r=[[*map(int, input().split())]for _ in 'a'*n]
    v=[0]*n
    s=[0]*201
    for i in r:
        if i[0]%2:
            i[0]+=1
        if i[1]%2:
            i[1]+=1
        if i[0]<i[1]:
            for j in range(i[0]//2,i[1]//2+1):
                s[j]+=1
        else:
            for j in range(i[1]//2,i[0]//2+1):
                s[j]+=1
    print('#%i' % t, max(s))

