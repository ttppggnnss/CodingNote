L=[[1,2,3,4,5],[6,7,8,9,0]]
L2=[L[0],L[1]]
L2[0][0]=9
print(L2)
print(L)
print()
L=[[1,2,3,4,5],[6,7,8,9,0]]
L3=[i for i in L]
L3[0][0]=8
print(L3)
print(L)
print()
L=[[1,2,3,4,5],[6,7,8,9,0]]
L4=[i[:] for i in L]
L4[0][0]=7
print(L4)
print(L)
print()
L=[[1,2,3,4,5],[6,7,8,9,0]]
L5=[L[0][:], L[1][:]]
L5[0][0]=6
print(L5)
print(L)