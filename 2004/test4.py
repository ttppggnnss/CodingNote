from itertools import combinations as c
from itertools import permutations as p
a=list(range(25))
d=0
for i in c(a,7):
    d+=1
print(d)
print('a')
i=list('abcabcabcabcabcab')
i1=sorted(i,key=lambda x:-i.count(x))
i2=sorted(i)
print(i)
print(i1)
print(i2)

