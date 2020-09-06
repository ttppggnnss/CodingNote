import sys
sys.stdin=open("input.txt","r")

for t in range(1,11):
    input();a=input();b=[];c=[]
    for i in a+' ':
        if i in "0123456789":c.append(int(i))
        elif i in "(":b.append(i)
        elif i in ")":
            while b[-1]!='(':c.append(b.pop())
            b.pop()
        elif i in "+":
            while b[-1] in '+*':c.append(b.pop())
            b.append(i)
        elif i in "*":
            while b[-1] in "*":c.append(b.pop())
            b.append(i)
        elif i in' ':
            while b:c.append(b.pop())
    for i in c:
        try:
            if i in '+*':
                if i=='+':b.append(b.pop(-2)+b.pop())
                else:b.append(b.pop(-2)*b.pop())
            else:b.append(i)
        except:b.append(i)
    print('#%i'%t,b[-1])