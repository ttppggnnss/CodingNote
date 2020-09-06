import sys
sys.stdin=open('input.txt','r')

d=lambda:map(int,input().split())
s=lambda i,v:v if i>11else min(s(i+1,v+t[i]*a),s(i+1,v+b),s(i+3,v+c))
for T in range(*d()):
    a,b,c,m=d()
    t=[*d()]
    print("#%d"%(T+1),min(s(0,0),m))