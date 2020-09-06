import sys
sys.stdin=open('input.txt','r')

def g(d,a,b,e):
    if d=='r':
        if saw_tooth[a][6]!=e:
            e = saw_tooth[a][2]
            if b==1:
                saw_tooth[a]=[saw_tooth[a][-1]]+saw_tooth[a][:-1]
                if a < 3:
                    g(d, a + 1, -b,e)
            if b==-1:
                saw_tooth[a]=saw_tooth[a][1:]+[saw_tooth[a][0]]
                if a < 3:
                    g(d, a + 1, -b,e)
    if d=='l':
        if saw_tooth[a][2]!=e:
            e=saw_tooth[a][6]
            if b==1:
                saw_tooth[a]=[saw_tooth[a][-1]]+saw_tooth[a][:-1]
                if a > 0:
                    g(d, a - 1, -b,e)
            if b==-1:
                saw_tooth[a]=saw_tooth[a][1:]+[saw_tooth[a][0]]
                if a > 0:
                    g(d, a - 1, -b,e)

def f(a,b):
    c=saw_tooth[a][2]
    d=saw_tooth[a][6]
    if b==1:
        saw_tooth[a]=[saw_tooth[a][-1]]+saw_tooth[a][:-1]
    if b==-1:
        saw_tooth[a]=saw_tooth[a][1:]+[saw_tooth[a][0]]
    if a<3:
        g('r',a+1,-b,c)
    if a>0:
        g('l',a-1,-b,d)

saw_tooth=[[*input()]for _ in'a'*4]
n=int(input())
for i in'a'*n:
    a,b=map(int,input().split())
    f(a-1,b)
print(int(saw_tooth[0][0])+int(saw_tooth[1][0])*2+int(saw_tooth[2][0])*4+int(saw_tooth[3][0])*8)