T = int(input())
for i in range(1, T + 1):
    n=float(input())
    if int(n*4096)!=(n*4096):
        print('#%d overflow'%i)
    else:
        ans=''
        for j in range(1, 13):
            if int(n*2)!=(n*2):
                ans+=str(int(n*2))
                n=n*2-int(n*2)
            else:
                ans+=str(int(n*2))
                break
        print('#%d'%i, ans)