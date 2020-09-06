arr=[7,4,2,0,0,6,0,7,0]
N=len(arr)

# arr[0] --> arr[N-1] 까지 밑에 오는 상자들이 있따면 낙차값
# h=N-1-0
# 모든 꼭대기의 상자에 대해서 반복 수행
ans=0
for i in range(N):
    h=N-1-i
    # 자기 밑에 오는 상자의 수를 카운팅
    for j in range(1,N):
        if arr[i]<=arr[j]:
            h-=1
    ans=max(ans,h)
print(ans)