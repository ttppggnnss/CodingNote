# 계산기3

import sys
sys.stdin=open("input.txt","r")

for t in range(1,11):
    n=int(input());a=[*input()];b=[]
    for _ in range(n):
        i=a.pop(0)
        if type(i)==int:
            a.insert(i,0)
            while b:a.append(b.pop())
        elif 48<=ord(i)<=57:a.append(int(i))
        elif i in "(":b.append(i)
        elif i in ")":
            while b[-1]!='(':a.append(b.pop())
            b.pop()
        elif i in "+":
            while b[-1] in '+*':a.append(b.pop())
            b.append(i)
        elif i in "*":
            while b[-1] in "*":a.append(b.pop())
            b.append(i)
    for i in a:
        if i=='+':b.append(b.pop(-2)+b.pop())
        elif i=='*':b.append(b.pop(-2)*b.pop())
        else:b.append(i)
    print('#%i'%t,*b)