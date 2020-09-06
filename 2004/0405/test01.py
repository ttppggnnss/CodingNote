def solution(inputString):
    cnt=0
    a=b=c=d=0
    for i in inputString:
        if i=='(':
            a+=1
        if i=='{':
            b+=1
        if i=='[':
            c+=1
        if i=='<':
            d+=1
        if i==')':
            if a>0:
                a-=1
                cnt+=1
            else:
                return -1
        if i=='}':
            if b>0:
                b-=1
                cnt+=1
            else:
                return -1
        if i==']':
            if c>0:
                c-=1
                cnt+=1
            else:
                return -1
        if i=='>':
            if d>0:
                d-=1
                cnt+=1
            else:
                return -1
    if a or b or c or d:
        return -1
    else:
        return cnt