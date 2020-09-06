import sys
sys.stdin=open('input.txt','r')

nums=['0001101','0011001','0010011','0111101','0100011','0110001','0101111','0111011','0110111','0001011']
for t in range(1,int(input())+1):
    n,m=map(int,input().split());ans=0;L=[input()[::-1] for _ in[0]*n]
    for i in L:
        if '1' in i:
            a=i.index('1');L2=[]
            for _ in range(8):
                L3=i[a:a+7][::-1]
                for j in range(10):
                    if L3==nums[j]:L2.append(j);break
                a+=7
            ans2=0;L2.reverse()
            for j in range(8):
                if j%2:ans2+=L2[j]
                else:ans2+=L2[j]*3
            if ans2%10==0:ans=sum(L2)
            break
    print('#%i'%t,ans)
