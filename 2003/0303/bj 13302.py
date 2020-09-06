import sys
sys.stdin=open('input.txt','r')
input=sys.stdin.readline

d1=10000
d3=25000
d5=37000
n,m=map(int,input().split())
V=[d1]*n+[0]*4
L=[*map(int,input().split())]
for i in L:
    V[i-1]=0

# 쿠폰 수
c=0
# 5일 연속 5일권
for i in range(n):
    if sum(V[i:i+5])==50000:
        V[i]=d5
        V[i+1]=0
        V[i+2]=0
        V[i+3]=0
        V[i+4]=0
# 3일 연속 3일권
for i in range(n):
    if sum(V[i:i+3])==30000:
        V[i]=d3
        V[i+1]=0
        V[i+2]=0
# 쿠폰 갯수
c=V.count(d3)+2*V.count(d5)

if c%3==2:
    for i in range(n):
        if sum(V[i:i+5])==d1+d2:
            V[i]=d5

            V[i+1]=0
            V[i+2]=0
            V[i+3]=0
            V[i+4]=0
            c+=1
            break

if V.count(d1)>(c//3):
    print(sum(V)-d1*(c//3))
else:
    print(sum(V)-d1*V.count(d1))
print(V)