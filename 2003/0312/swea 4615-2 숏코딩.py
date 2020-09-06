d=[0,1,-1]
for T in range(int(input())):
    N,M=map(int,input().split());S=[[0]*(N+1) for i in range(N+1)];S[N//2][N//2]=2;S[N//2+1][N//2]=1;S[N//2][N//2+1]=1;S[N//2+1][N//2+1]=2
    for m in range(M):
        Y,X,Z=map(int,input().split());S[Y][X]=Z
        for i in d:
            for j in d:
                y=Y+i;x=X+j;c=0
                while not(i==j==0)and  y>0and x>0and y<N+1and x<N+1:
                    c+=1
                    if not S[y][x]:break
                    if S[y][x]==Z:
                        for p in range(c):S[Y+i*p][X+j*p]=Z

                        break
                    y+=i;x+=j
    print("#%d"%(T+1),sum(1for i in sum(S,[])if i==1),sum(1for i in sum(S,[])if i==2))