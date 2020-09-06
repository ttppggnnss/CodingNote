import sys
sys.stdin=open('input.txt','r')

for t in range(1,int(input())+1):
    h,w=map(int,input().split())
    M=[[*input()] for _ in [0]*h]
    n=int(input())
    order=[*input()]
    for i in range(w):
        for j in range(h):
            if M[j][i] in '<>^v':
                st0,st1=j,i
    for s in order:
        if s=='S':
            if M[st0][st1]=='v':
                y=1
                if st0+y<h-1:
                    while M[st0+y][st1]in '.-':
                        y+=1
                        if st0+y>=h-1:break
                if st0+y<h and M[st0+y][st1]=='*':
                    M[st0+y][st1]='.'
            elif M[st0][st1]=='^':
                y=-1
                if st0+y>0:
                    while M[st0+y][st1]in '.-':
                        y-=1
                        if st0+y<=0:break
                if st0+y>=0 and M[st0+y][st1]=='*':
                    M[st0+y][st1]='.'
            elif M[st0][st1] == '>':
                x = 1
                if st1+x<w-1:
                    while M[st0][st1+x]in '.-':
                        x += 1
                        if st1+x>=w-1: break
                if st1+x<w and M[st0][st1+x] == '*':
                    M[st0][st1+x] = '.'
            elif M[st0][st1] == '<':
                x = -1
                if st1+x>0:
                    while M[st0][st1 + x]in '.-':
                        x -= 1
                        if st1 + x<=0: break
                if st1+x>=0 and M[st0][st1 + x] == '*':
                    M[st0][st1 + x] = '.'
        elif s=='U':
            M[st0][st1]='^'
            if st0-1>=0 and M[st0-1][st1]=='.':
                M[st0][st1],M[st0-1][st1]=M[st0-1][st1],M[st0][st1]
                st0-=1
        elif s == 'D':
            M[st0][st1] = 'v'
            if st0 + 1 <h and M[st0+1][st1] == '.':
                M[st0][st1], M[st0 + 1][st1] = M[st0 + 1][st1], M[st0][st1]
                st0+=1
        elif s== 'R':
            M[st0][st1]='>'
            if st1+1<w and M[st0][st1+1]=='.':
                M[st0][st1],M[st0][st1+1]=M[st0][st1+1],M[st0][st1]
                st1+=1
        elif s== 'L':
            M[st0][st1]='<'
            if st1-1>=0 and M[st0][st1-1]=='.':
                M[st0][st1],M[st0][st1-1]=M[st0][st1-1],M[st0][st1]
                st1-=1
    print('#%i'%t, end=" ")
    for i in M:
        print(*i, sep='')