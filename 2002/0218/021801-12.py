# 계산기3

import sys
sys.stdin=open("input.txt","r")

def cal(s):
    a=[]
    for i in s:
        if i.isdigit():
            a.append(int(i))
            if a[-2]=='*':a.append(a.pop(-3)*a.pop());a.pop(-2)
        elif i==')':
            while a[-2]!='(':
                if a[-2]=='+':a.append(a.pop(-3)+a.pop());a.pop(-2)
            a.pop(-2)
        elif i=='+':
            if a[-2]=='(':a.append(i)
            elif a[-2]=='+':a.append(a.pop(-3)+a.pop())
            else:a.pop(-2);a.append(i);a.append(a.pop(-3)*a.pop(-2));
        elif i=='*':
            if a[-2]=='*':a.append(a.pop(-3)*a.pop())
            else:a.append(i)
        else:a.append(i)
    return a
for t in range(1,11):
    input();print('#%d'%t,*cal(input()))

# for t in range(1,11):
#     input();a=[];b=[];
#     for i in input():
#         if i.isdigit():a.append(int(i));
#         elif i==')':
#             while b[-1]!='(':
#                 if b.pop()=='*':a.append(a.pop(-2)*a.pop());
#                 else:a.append(a.pop(-2)+a.pop());
#             b.pop()
#         elif i=='+':
#             if b[-1]=='(':b.append(i);
#             elif b[-1]=='+':a.append(a.pop(-2)+a.pop());
#             else:b.pop();a.append(a.pop(-2)*a.pop());b.append(i);
#         elif i=='*':
#             if b[-1]=='*':a.append(a.pop(-2)*a.pop());
#             else:b.append(i);
#         else:b.append(i);
#     print('#%d %d'%(t,a.pop()));