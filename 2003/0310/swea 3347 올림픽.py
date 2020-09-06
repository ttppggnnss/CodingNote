for t in range(1, int(input())+1):
    input();A=[*map(int,input().split())];B=[*map(int,input().split())];C=[0]*1001
    for i in B:
       	for k,j in enumerate(A,1):
            if j<=i:C[k]+=1;break
    print('#%i'%t,C.index(max(C)))