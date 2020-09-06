# wrong answer
import sys
sys.stdin=open('../input.txt','r')

for t in range(1,int(input())+1):
    s=[*input()]
    if s[0]=='1':
        s.insert(0,'(')
    i=0
    while i<len(s)-1:
        if s[i]=='0' and s[i+1]=='1':
            s.insert(i+1,'(')
        if s[i]=='1' and s[i+1]=='0':
            s.insert(i+1,')')
        i+=1
    if s[-1]=='1':
        s.append(')')
    print('Case #%i: ',*s,sep="")