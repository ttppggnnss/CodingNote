# 계산기3

import sys
sys.stdin=open("input.txt","r")

def f(a):
    b = [];c = []
    for i in a + ' ':
        if i.isdigit():c.append(int(i))
        elif i in "(":b.append(i)
        elif i in ")":
            while b[-1] != '(': c.append(b.pop())
            b.pop()
        elif i in "+":
            while b[-1] in '+*': c.append(b.pop())
            b.append(i)
        elif i in "*":
            while b[-1] in "*": c.append(b.pop())
            b.append(i)
        elif i in ' ':
            while b: c.append(b.pop())
    for i in c:
        if i == '+':
            b.append(b.pop(-2) + b.pop())
        elif i == '*':
            b.append(b.pop(-2) * b.pop())
        else:b.append(i)
    return b[-1]
for t in range(1,11):input();print('#%i'%t,f(input()))