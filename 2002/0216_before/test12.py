import sys
sys.stdin=open("input12.txt","r")
for t in range(1,int(input())+1):
    input()
    s=input()
    stack=[]
    top=-1
    c=[]
    tmp=0
    for i in s+' ':
        if i in "0123456789"and tmp==0:
            c.append(i)
            tmp=1
        elif i in "0123456789"and tmp==1:
            c[-1]+=i
        elif i in "(":
            stack.append(i)
            top+=1
            tmp=0
        elif i in ")":
            while stack[top]!='(':
                c.append(stack.pop())
                top-=1
            stack.pop()
            top-=1
            tmp=0
        elif i in "+-":
            while stack[top] in '+-*/':
                c.append(stack.pop())
                top-=1
            stack.append(i)
            top+=1
            tmp=0
        elif i in "*/":
            while stack[top] in "*/":
                c.append(stack.pop())
                top-=1
            stack.append(i)
            top+=1
            tmp=0
        elif i in' ':
            while top>-1:
                c.append(stack.pop())
                top-=1
    stack2=[]
    for i in c:
        if i in '+-*/':
            if i=='+':
                stack2.append(str(int(stack2.pop(-2))+int(stack2.pop())))
            if i == '-':
                stack2.append(str(int(stack2.pop(-2))-int(stack2.pop())))
            if i == '*':
                stack2.append(str(int(stack2.pop(-2))*int(stack2.pop())))
            if i == '/':
                stack2.append(str(int(stack2.pop(-2))/int(stack2.pop())))
        else:
            stack2.append(i)
    print('#%i'%t,int((float(stack2[-1]))))