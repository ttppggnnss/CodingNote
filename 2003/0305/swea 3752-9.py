import sys
sys.stdin=open('input.txt','r')

for t in range(1,1+int(input())):
    input()
    points=map(int, input().split())
    ans=1
    for point in points:
        print(point)
        ans|=ans<<point
        print(bin(ans))
    print('#%d'%t, bin(ans).count('1'))