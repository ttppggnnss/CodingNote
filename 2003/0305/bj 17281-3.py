from itertools import permutations as p
n=int(input())
I=[[*map(int,input().split())]for _ in'a'*n]
ans=0
for l in p(range(1,9),8):
    l=list(l)
    l.insert(3,0)
    cnt = 0
    score = 0
    for i in I: # range(n) 으로 해서 I[i] 하면 시간 초과가 된다
        out = 0
        b1, b2, b3 = 0, 0, 0
        while out < 3:
            k=i[l[cnt]]
            if k == 0: out += 1
            if k == 1: score += b3;b1, b2, b3 = 1, b1, b2
            if k == 2: score += b2 + b3;b1, b2, b3 = 0, 1, b1
            if k == 3: score += b1 + b2 + b3;b1, b2, b3 = 0, 0, 1
            if k == 4: score += b1 + b2 + b3 + 1;b1, b2, b3 = 0, 0, 0
            cnt = (cnt + 1) % 9
    ans=max(ans,score)
print(ans)