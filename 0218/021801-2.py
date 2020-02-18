# 계산기 3

import sys
sys.stdin=open("input.txt","r")

for t in range(1,11):
    input();a=input();b=[];c=''
    for i in a+' ':
        if i in "0123456789":c+=i
        elif i in "(":b.append(i)
        elif i in ")":
            while b[-1]!='(':c+=b.pop()
            b.pop()
        elif i in "+":
            while b[-1] in '+*':c+=b.pop()
            b.append(i)
        elif i in "*":
            while b[-1] in "*":c+=b.pop()
            b.append(i)
        elif i in' ':
            while b:c+=b.pop()
    for i in c:
        if i=='+':b.append(b.pop(-2)+b.pop())
        elif i=='*':b.append(b.pop(-2)*b.pop())
        else:b.append(int(i))
    print('#%i'%t,b[-1])