# 5점 획득
# 11점 미획득 (효율성?)

# 4
# 0000
# 101
# 111000
# 1

import sys
sys.stdin=open('../input.txt','r')

for t in range(1,int(input())+1):
    s=input()
    c=''
    add=''
    for i in s:
        if i=='1' and add=='':
            add+='('+i
        elif i=='1':
            add+=i
        elif add!='':
            c+=add+')'
            c+=i
            add=''
        else:
            c+=i
    if add!='':
        c+=add+')'
    print('Case #%i:'%t,c)