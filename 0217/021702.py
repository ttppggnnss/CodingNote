L=list(range(1,11))
L2=[]
def backtrack(L,L2):
    if sum(L2)==10:
        print(L2)
    if sum(L2)>10:
        return
    for k,v in enumerate(L):
        L2.append(v)
        L.remove(v)
        backtrack(L[k:],L2)
        L2.remove(v)
        L.insert(k,v)
backtrack(L,L2)