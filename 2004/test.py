A=['a','b','c']
ans=[]
for i in range(1<<3):
    B=[]
    for j in range(3):
        if i&(1<<j):
            B.append(A[j])
    ans.append(B)
print(*ans)

arr='ABCD'; N=len(arr)
bit=[0]*N
C=[]
def subset(k,n):
    if k==N:
        print(len(C), C)
    else:
        C.append(arr[k])
        subset(k+1, N)
        C.pop()
        subset(k+1, N)

subset(0,N)
print()
D=[]
# 중복 있는 순열
def permutations(k,n):
    if k==n:
        print(len(D),D)
    else:
        for i in range(N):
            D.append(arr[i])
            permutations(k+1,n)
            D.pop()

permutations(0,3)
print()
E=[]
# 중복 없는 순열
def permutations2(k,n,bit):
    if k==n:
        print(len(D),D)
    else:
        for i in range(N):
            if bit&(1<<i):continue
            D.append(arr[i])
            permutations2(k+1,n,bit|(1<<i))
            D.pop()
permutations2(0,3,0)
