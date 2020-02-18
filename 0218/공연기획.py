import sys
sys.stdin=open('공연기획.txt','r')

for t in range(1,int(input())+1):
    clap=input()
    hire=0;c=0
    for i in range(len(clap)):
        if c>=i:c+=int(clap[i])
        else:
            hire1=0
            while c+hire1 != i:
                hire1+=1
            hire+=hire1
            c=i+int(clap[i])
    print('#%d'%t,hire)