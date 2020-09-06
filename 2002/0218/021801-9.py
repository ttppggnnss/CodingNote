# 계산기3

import sys
sys.stdin=open("input.txt","r")

for t in range(1,11):
    input();s=[]
    for i in input():
        if i.isdigit():
            if s[-1]=='*':s.pop();s.append(s.pop()*int(i))
            else:s.append(int(i))
        elif i==')':
            while s[-2]!='(':s.append(s.pop(-3)+s.pop());s.pop(-2)
            s.pop(-2)
            if len(s)>2 and s[-2]=='*':
                s.append(s.pop(-3)*s.pop());s.pop()
        else:s.append(i)
    print("#%d %d"%(t,s[0]))