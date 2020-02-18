# 계산기3

import sys
sys.stdin=open("input.txt","r")

for t in range(1,11):
    input();s=[]
    for i in input():
        try:
            s.append(int(i))
            if s[-2]=='*':
                s[-3]*=s[-1]
                del s[-2:]
        except:
            if i==')':
                while s[-2]!='(':
                    s[-3]+=s[-1]
                    del s[-2:]
                del s[-2]
                if len(s)>2 and s[-2]=='*':
                    s[-3]*=s[-1]
                    del s[-2:]
            else:
                s.append(i)
    print("#%d %d"%(t,s[0]))