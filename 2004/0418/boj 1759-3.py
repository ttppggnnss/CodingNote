import sys
sys.stdin=open('../input.txt','r')

from itertools import combinations as c
L,C = map(int,input().split())
strs=sorted([*input().split()])
for i in c(strs,L):
    vowel=0
    consonant=0
    for z in i:
        if z in 'aeiou':
            vowel+=1
        else:
            consonant+=1
        if vowel>0 and consonant>1:
            print(*i,sep="")
            break