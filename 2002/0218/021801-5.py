# 계산기3

import sys
sys.stdin=open("input.txt","r")

for t in range(1, 11):
    a=[];b=[];input()
    for i in input():
        if i == '(':b.append(i)
        elif i == '*':
            try:
                if b[-1]!='*':b.append(i)
                else:a.append(a.pop(-2)*a.pop())
            except:a.append(a.pop(-2)*a.pop())
        elif i == '+':
            try:
                if b[-1]=='(':b.append(i)
                elif b[-1]=='*':b.pop();a.append(a.pop(-2)*a.pop());b.append(i)
                else:a.append(a.pop(-2)+a.pop())
            except:a.append(a.pop(-2)+a.pop())
        elif i == ')':
            while b[-1]!='(':
                if b.pop()=='+':a.append(a.pop(-2)+a.pop())
                else:a.append(a.pop(-2)*a.pop())
            b.pop()
        else:a.append(int(i))
    print('#%i'%t,a.pop())