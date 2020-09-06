import sys
sys.stdin=open('../input.txt','r')

def c(strs,p=[]):
    if len(p)==L:
        for k in 'aeiou':
            if k in p:
                a = L
                for z in 'aeiou':
                    a -= p.count(z)
                if a > 1:
                    print(*p, sep="")
                    break
    else:
        for i in range(len(strs)):
            p.append(strs[i])
            c(strs[i+1:],p)
            p.pop()

L,C = map(int,input().split())
strs=[*input().split()]
strs=sorted(strs)
c(strs,[])