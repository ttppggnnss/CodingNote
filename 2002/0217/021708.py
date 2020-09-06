L=list(range(1,11))
L2=[]
def backtrack(L,L2):
    if len(L2)==3:
        print(L2)
    for k,v in enumerate(L):
        L2.append(v)
        L.remove(v)
        backtrack(L,L2)
        L2.remove(v)
        L.insert(k,v)

backtrack(L,L2)