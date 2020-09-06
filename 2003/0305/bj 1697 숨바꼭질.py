# runtime error
import sys
sys.stdin=open('input.txt','r')
input=sys.stdin.readline
sys.setrecursionlimit=100000000

def f(n,k,cnt=0):
    v[n]=1
    global ans
    if cnt>ans:return
    if n>2*k:return
    if n==k:ans=min(ans,cnt);return
    if v[2*n]<1:f(2*n,k,cnt+1);v[2*n]=0
    if v[n-1]<1:f(n-1,k,cnt+1);v[n-1]=0
    if v[n+1]<1:f(n+1,k,cnt+1);v[n+1]=0

n,k=map(int,input().split());ans=9**9;v=[0]*100001;f(n,k);print(ans)