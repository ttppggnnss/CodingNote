import sys
sys.stdin=open('algo3.txt','r')

# 'w' 면 1, 'b' 면 0 인 사전을 선언한다
dic={'w':'1','b':'0'}

# 함수 선언
def zzip(S,N): # 사각형과 사각형의 크기를 입력받는다
    if N==1: # N=1 일 때 즉 사각형의 크기가 2x2 일 떄
        if S[0][0]==S[0][1]==S[1][0]==S[1][1]=='w':
            return '1' # 전부 흰색이면 '1' 반환
        elif S[0][1]==S[0][1]==S[1][0]==S[1][1]=='b':
            return '0' # 전부 검은색이면 '0' 반환
        else:
                        # 둘 다 아니면 x 이후에 각각의 색상을 입력한다
            return 'x'+dic[S[0][0]]+dic[S[0][1]]+dic[S[1][0]]+dic[S[1][1]]
    else: # N이 1이 아닐 때
        # 왼쪽 위 사각형
        S1=[[0]*2**(N-1) for _ in range(2**(N-1))]
        # 새로운 사각형을 가로 세로 각각 사각형 S의 2분의 1 크기 (전체의 4분의 1 크기) 로 비워서 만든다.
        for i in range(2**(N-1)):
            for j in range(2**(N-1)):
                S1[i][j]=S[i][j]
                # 사각형 S 의 왼쪽 위 4분의 1과 똑같이 채워준다
        a=zzip(S1,N-1) # a에는 zzip(S1,N-1) 을 받는다.

        # 이하 동일한 방법으로 나머지 사각형을 구해준다.

        # 오른쪽 위 사각형
        S2=[[0]*2**(N-1) for _ in range(2**(N-1))]
        for i in range(2**(N-1)):
            for j in range(2**(N-1)):
                S2[i][j]=S[i][j+2**(N-1)]
        b=zzip(S2,N-1)

        # 왼쪽 아래 사각형
        S3=[[0]*2**(N-1) for _ in range(2**(N-1))]
        for i in range(2**(N-1)):
            for j in range(2**(N-1)):
                S3[i][j]=S[i+2**(N-1)][j]
        c=zzip(S3,N-1)

        # 오른쪽 아래 사각형
        S4=[[0]*2**(N-1) for _ in range(2**(N-1))]
        for i in range(2**(N-1)):
            for j in range(2**(N-1)):
                S4[i][j]=S[i+2**(N-1)][j+2**(N-1)]
        d=zzip(S4,N-1)

        if a==b==c==d=='1': # a,b,c,d 가 모두 '1' 이면 '1'을 반환한다
            return '1'
        elif a==b==c==d=='0': # a,b,c,d 가 모두 '0' 이면 '0'을 반환한다
            return '0'
        else:
            return 'x'+a+b+c+d


# 사각형의 정보를 입력받는다
N=int(input())
S=[[*input()]for _ in range(2**N)] # 2^N 개씩 2^N 줄 입력받는다.

# zzip(S,N) 을 출력한다
print(zzip(S,N))