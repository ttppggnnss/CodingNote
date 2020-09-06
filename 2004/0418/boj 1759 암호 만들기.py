import sys
sys.stdin=open('../input.txt','r')

def combi(arr,start,r):
    if r<1 or not arr: return [[]]
    for i in range(start, len(arr)-r+1):
        if r==1:
            yield [arr[i]]
        else:
            for j in combi(arr,i+1,r-1):
                yield [arr[i]]+j

L,C = map(int,input().split())
strs=[*input().split()]
strs=sorted(strs)
for i in combi(strs,0,L):
    for k in 'aeiou':
        if k in i:
            a=L
            for z in 'aeiou':
                a-=i.count(z)
            if a>1:
                print(*i,sep="")
                break
    else:
        pass