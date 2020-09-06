# 오답
import sys
sys.stdin=open('input.txt','r')

# 수정 본 실행시간 반으로 줄어듬
for t in range(1,int(input())+1):
    n, k = map(int,input().split());cnt=0
    L=[*map(int,input().split())];q=[(0,-1)]
    while q:
        a,b=q.pop()
        for id,v in enumerate(L):
            if id>b:
                a+=v
                if a>k:
                    a-=v
                    if a<k:q.append((a,id))
                elif a<k:q.append((a,id))
                elif a==k:cnt+=1;print(a,id)
                a-=v
    print("#%i"%t, cnt)
