import sys
sys.stdin=open('input.txt','r')

for t in range(1, int(input())+1):
    a,b=input().split()
    c='';d=0
    for i in range(1,max(len(a),len(b))+1):
        if i <=len(a):a1=ord(a[-i])-ord('0')
        else:a1=0
        if i<=len(b):b1=ord(b[-i])-ord('0')
        else:b1=0
        s=a1+b1+d
        if s>9:c+=str(s-10);d=1
        else:c+=str(s);d=0
    c+=str(d)
    c=c[::-1].lstrip('0')
    print('#%i'%t,c)