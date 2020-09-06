import sys
sys.stdin=open('input.txt','r')

for t in range(1, int(input())+1):
    buses=[[*map(int,input().split())] for _ in [0]*int(input())]
    stops=[int(input()) for _ in [0]*int(input())]
    ans=[]
    for i in stops:
        ans.append(sum([1 for j in buses if j[0]<=i<=j[1]]))
    print('#%i'%t,*ans)