# 계산기3

import sys
sys.stdin=open("input.txt","r")

for t in range(1,11):
    input();a=[];b=[]
    for i in input():
        if i.isdigit():a.append(int(i))
        elif i==')':
            while b[-1]!='(':
                if b.pop()=='*':a.append(a.pop(-2)*a.pop())
                else:a.append(a.pop(-2)+a.pop())
            b.pop()
        elif i=='+':
            if b[-1]=='(':b.append(i)
            elif b[-1]=='+':a.append(a.pop(-2)+a.pop())
            else:a.append(a.pop(-2)*a.pop());b.pop();b.append(i)
        elif i=='*':
            if b[-1]=='*':a.append(a.pop(-2)*a.pop())
            else:b.append(i)
        else:b.append(i)
    print('#%i'%t,a.pop())