u=input
for t in range(1,1+int(u())):
    u();s=map(int,u().split());a=1
    for i in s:a|=a<<i
    print('#%i'%t,bin(a).count('1'))