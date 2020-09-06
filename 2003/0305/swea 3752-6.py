# 통과
import sys
sys.stdin=open('input.txt','r')

for t in range(1,1+int(input())):
    input();s=[*map(int,input().split())];a={0}
    for i in s:a=a|set([j+i for j in a])
    print('#%i'%t,len(a))
