for t in range(1,int(input())+1):
    n=int(input());numbs=[*map(int, input().split())]
    # 선택 정렬
    for i in range(0,10):
        idx=i
        if i&1:
            for j in range(i+1,n):
                if numbs[idx]<numbs[j]:idx=j
            numbs[i],numbs[idx]=numbs[idx],numbs[i]
        else:
            for j in range(i+1,n):
                if numbs[idx]>numbs[j]:idx=j
            numbs[i],numbs[idx]=numbs[idx],numbs[i]
    print('#%i'%t,*numbs[:10])