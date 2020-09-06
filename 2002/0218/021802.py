# 4874 Forth

import sys
sys.stdin=open("input2.txt","r")

for t in range(1,int(input())+1):
    s=[*input().split()];b=[]
    for i in s:
        try:
            if i=='+':b.append(b.pop(-2)+b.pop())
            elif i=='-':b.append(b.pop(-2)-b.pop())
            elif i=='*':b.append(b.pop(-2)*b.pop())
            elif i=='/':b.append(b.pop(-2)//b.pop())
            elif i=='.':break
            else:b.append(int(i))
        except:
            b.append('error')
            break
    if len(b)!=1:
        b.append('error')
    print("#%i"%t,b[-1])