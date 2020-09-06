import sys
sys.stdin=open('input.txt','r')

for t in range(1,int(input())+1):
    origin_memory=input()
    cnt=0
    for i in range(len(origin_memory)-1):
        if origin_memory[i]!=origin_memory[i+1]:
            cnt+=1
    if origin_memory[0]=='1':
        cnt+=1
    print('#%i'%t,cnt)
