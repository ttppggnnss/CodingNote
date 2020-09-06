# 숏코딩 # 백준 메모리 초과

n=int(input())
L=[[]for i in range(n)]
L[0]=[[i]for i in range(n)] # 첫 줄 초기화 0 ~ n-1
for i in range(1,n):
    for j in range(n):
        for p in L[i-1]: # 이전 줄에 대해서
            for y,x in enumerate(p): # L[0]=[[0],[1],[2],[3],...[n-1]] # y,x = 0,0, 1,1, 2,2, 3,3, 4,4, 5,5, ...
                if j==x or j-x==i-y or x-j==i-y: # 0~n 중 j 가 0~n-1 과 같거나 j-x 가 i-y 와 같거나 x-j 와 i-y 가 같으면 멈춘다
                    break
            else: # 아니면 L[i] 에 [ L[i-1]+L[j] ] 를 더한다 즉 L[i-1]+L[j] 가 마지막 항에 추가된다
                L[i]+=[p+[j]]
            print()
            for k in L:
                print(*k)
print(len(L[-1]))