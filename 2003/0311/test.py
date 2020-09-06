L=[[1,2,3,4,5],[6,7,8,9,0]]
L2=L[:]
print(L2, 'L2')
L2[0]=[5,4,3,2,1]
print(L2, 'L2 통으로 바꿈')
print(L, 'L')
L2[0][0]=9
print(L2, 'L2 부분 바꿈')
print(L, 'L')
L2[1][0]=0
print(L2, 'L2 한 번 더 부분 바꿈')
print(L, 'L')

print()
L3=[[1,2,3,4,5],[6,7,8,9,0]]
L4=L3[:]
print(L4, 'L4')
L4[0][0]=5
print(L4, 'L4 바굼')
print(L3, 'L3')

print()
L5=[1,2,3,4,5]
L6=L5[:]
print(L6, 'L6')
L6[0]=5
print(L6, 'L6 바꿈')
print(L5, 'L5')