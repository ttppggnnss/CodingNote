# 황수현 풀이
import sys
sys.stdin=open('input.txt','r')
for t in range(1,int(input())+1):
    n,k=map(int,input().split())
    num=input()
    num2=[]
    tmp=int(n/4)
    num2+=[num[0:tmp]]
    num2+=[num[tmp: tmp*2]]
    num2+=[num[tmp*2:  tmp*3]]
    num2+=[num[tmp*3:]]
    for i in range(tmp-1):
        num=num[1:]+num[0]
        num2 += [num[0:tmp]]
        num2 += [num[tmp: tmp * 2]]
        num2 += [num[tmp * 2:  tmp * 3]]
        num2 += [num[tmp * 3:]]
    num2=list(map(lambda x:int(x,16),set(num2)))
    num2.sort(reverse=True)
    print("#%d %d"%(t,num2[k-1]))