# 1. 숫자 이동
# import sys
# sys.stdin=open('../input.txt','r')

def f(A):
    B=[0]*10 # A와 크가 같고 비어있는 배열을 만든다.
    for i in range(10):
        if i==0 and abs(A[i])>=10: # 가장 왼쪽의 숫자가 움직일 때 절댓값 10보다 크면
            B[i]+=abs(A[i]//2)
            B[i+1]+=abs(A[i]//2)
        elif i==0: # 가장 왼쪽의 숫자가 움직일 때 절댓값 10보다 작은 경우
            if A[i]<0:
                B[i]-=A[i]
            else:
                B[i+1]+=A[i]
        elif i==9 and abs(A[i])>=10: # 가장 오른쪽 숫자가 움직일 때 절댓값 10보다 크면
            B[i]-=abs(A[i]//2)
            B[i-1]-=abs(A[i]//2)
        elif i==9: # 가장 오른쪽 숫자가 움직이 ㄹ때 절댓값 10보다 작으면
            if A[i]>0:
                B[i]-=A[i]
            else:
                B[i-1]+=A[i]
        elif abs(A[i])>=10: # 나머지 숫자 움직일 때 절댓값 10보다 크면
            B[i+1]+=abs(A[i]//2)
            B[i-1]-=abs(A[i]//2)
        else: # 나머지 숫자 움직일 때 절댓값 10보다 작으면
            if A[i]>0:
                B[i+1]+=A[i]
            else:
                B[i-1]+=A[i]
    return B

for t in range(1,int(input())+1): # 1부터 입력받은 숫자 만큼 반복한다
    N=int(input()) # N 을 입력받는다
    A=[*map(int,input().split())] # 10개의 숫자를 A에 입력받는다
    for i in range(N): # N 이동시간 동안 이동한다
        A=f(A) # 이동한 값으로 바뀐다
    print('#%i'%t,*A)