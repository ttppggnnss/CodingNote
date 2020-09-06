import sys
sys.stdin=open('input.txt','r')

def bt(k, a):
    global M
    if M >= a: return
    if k == n: M=max(M,a);return
    for i in range(n):
        if v[i]<1:v[i]=1;bt(k+1,a*L[i][k]);v[i]=0
u=input
for t in range(1, int(u()) + 1):n=int(u());L=[[*map(lambda x:x/100,map(int, u().split()))] for _ in'a'*n];M=0;v=[0]*n;bt(0,1);print("#%i %.6f"%(t,M*100))
