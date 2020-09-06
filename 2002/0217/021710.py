import sys
sys.stdin=open("input021710.txt","r")

for t in range(1,11):
    input();s=input();stack=[];c=''
    for i in s+' ':
        if i in "0123456789":c+=i
        elif i in "(":stack.append(i)
        elif i in ")":
            while stack[-1]!='(':c+=stack.pop()
            stack.pop()
        elif i in "+":
            while stack[-1] in '+*':c+=stack.pop()
            stack.append(i)
        elif i in "*":
            while stack[-1] in "*":c+=stack.pop()
            stack.append(i)
        elif i in' ':
            while stack:c+=stack.pop()
    for i in c:
        if i in '+*':
            if i=='+':stack.append(str(int(stack.pop(-2))+int(stack.pop())))
            if i == '*':stack.append(str(int(stack.pop(-2))*int(stack.pop())))
        else:stack.append(i)
    print('#%i'%t,int((stack[-1])))