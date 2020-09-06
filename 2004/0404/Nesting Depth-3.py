# 5점 획득
# 11점 미획득
import sys
sys.stdin=open('../input.txt','r')

for t in range(1,int(input())+1):
    s=input()
    c=''
    if s[0]=='1':
        c+='('
    for i in range(len(s)-1):
        if s[i]=='0' and s[i+1]=='1':
            c+=s[i]+'('
        elif s[i]=='1' and s[i+1]=='0':
            c+=s[i]+')'
        else:
            c+=s[i]
    if s[-1]=='1':
        c+='1'+')'
    else:
        c+='0'
    print('Case #%i:'%t,c)