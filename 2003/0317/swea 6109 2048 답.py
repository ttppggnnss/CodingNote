def f(N, tile):
    ans = [[0]*N for _ in range(N)]
    for r in range(N):
        st = []
        for i in range(N):
            if tile[r][i]!=0:   # 0을 제거
                st.append(tile[r][i])
        i = N-1                 # 오른쪽 칸부터 채움
        while len(st)>=2:        # 2개 이상이면
            a = st.pop()        # 2개의 숫자를 꺼내
            b = st.pop()
            if a==b:            # 두 개가 같으면
                ans[r][i] = a + b # 더해서 넣고
            else:               # 숫자가 다르면
                ans[r][i] = a   # 먼저 꺼낸 숫자를 쓰고
                st.append(b)    # 나중에 꺼낸 숫자는 다시 돌려놓음
            i -= 1              # 왼쪽 칸 채우러 이동
        if st: # 1개 남은 경우
            ans[r][i] = st.pop()    # 남은 숫자로 채움
    return ans

def cw(N, org):
    dest = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            dest[i][j] = org[N-1-j][i]
    return dest


T = int(input())
for tc in range(1, T+1):
    s = list(input().split())
    N = int(s[0])
    S = s[1]
    tile = [list(map(int, input().split())) for i in range(N)]
    ans = []
    if S=='right':
        ans = f(N, tile)
    elif S=='up':
        tile = cw(N, tile)
        ans = f(N, tile)
        for _ in range(3):
            ans = cw(N, ans)
    elif S=='left':
        tile = cw(N, tile)
        tile = cw(N, tile)
        ans = f(N, tile)
        ans = cw(N, ans)
        ans = cw(N, ans)
    elif S=='down':
        for _ in range(3):
            tile = cw(N, tile)
        ans = f(N, tile)
        ans = cw(N, ans)

    print('#{} '.format(tc))
    for i in range(N):
        for j in range(N):
            print(ans[i][j], end=' ')
        print()
