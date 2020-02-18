# 계산기3

import sys
sys.stdin=open("input.txt","r")
def f(a):
    s=[]
    for i in a:
        try:
            s.append(int(i))
            if s[-2] == '*':
                s[-3] *= s[-1]
                del s[-2:]
        except:
            if i == ')':
                while s[-2] != '(':
                    s[-3] += s[-1]
                    del s[-2:]
                del s[-2]
                if len(s) > 2 and s[-2] == '*':
                    s[-3] *= s[-1]
                    del s[-2:]
            else:s.append(i)
    return s[0]
for t in range(1,11):input();print('#%d'%t,f(input()))