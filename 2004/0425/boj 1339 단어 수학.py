# 접근방식 잘못됨

import sys
sys.stdin=open('../input.txt','r')

def change(i,words):
    cnt=0
    for word in words:
        for k in range(len(word)):
            cnt+=(9-i.index(word[-k-1]))*(10**k)
    return cnt

n=int(input())
words=[]
words3=[[] for _ in range(8)]
for i in range(n):
    words.append(input())

for word in words:
    for k in range(len(word)):
        words3[k].append(word[-k-1])

q=[]
print(words3)
for i in words3[::-1]:
    if i!={}:
        i.sort(key=lambda x:(words3[::-1][0].count(x), words3[::-1][1].count(x), words3[::-1][2].count(x),words3[::-1][3].count(x),words3[::-1][4].count(x),words3[::-1][5].count(x),words3[::-1][6].count(x),words3[::-1][7].count(x)))
        print(i)
        for j in i:
            if j not in q:
                q.append(j)
print(q)
ans=change(q,words)
print(ans)