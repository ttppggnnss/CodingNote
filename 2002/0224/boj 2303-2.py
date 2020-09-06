# https://www.acmicpc.net/problem/2303
# combinations 만들어 쓰기
import sys
sys.stdin=open('input.txt','r')
def combinations(arr,r):
    arr=sorted(arr)
    V=[i for i in arr]
    L2=[]
    def generate(chosen):
        if len(chosen)==r and sorted(chosen) not in L2:
            L3=[i for i in sorted(chosen)]
            L2.append(L3)
        for i,x in enumerate(V):
            V.remove(x)
            chosen.append(x)
            generate(chosen)
            chosen.pop()
            V.insert(i,x)
    generate([])
    return L2

ans1=0;ans2=0
for i in range(int(input())):
    for j in combinations([*map(int,input().split())],3):
        if ans1<=sum(j)%10:ans1=sum(j)%10;ans2=i+1
print(ans2)