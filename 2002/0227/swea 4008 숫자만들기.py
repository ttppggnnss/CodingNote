import sys
sys.stdin=open('input.txt','r')

def cal(num, idx, add, sub, multi, divi):
    global n, mx, mn
    if idx==n:
        mx=max(num,mx)
        mn=min(num,mn)
        return
    else:
        if add:
            cal(num+num_list[idx],idx+1,add-1,sub,multi,divi)
        if sub:
            cal(num-num_list[idx],idx+1,add,sub-1,multi,divi)
        if multi:
            cal(num*num_list[idx],idx+1,add,sub,multi-1,divi)
        if divi:
            if num>0:
                cal(num//num_list[idx],idx+1,add,sub,multi,divi-1)
            else:
                cal(-((-num)//num_list[idx]),idx+1,add,sub,multi,divi-1)

for t in range(1,int(input())+1):
    n=int(input())
    a,b,c,d=map(int,input().split())
    num_list=[*map(int,input().split())]
    mx=-1000000000000
    mn=1000000000000
    cal(num_list[0],1,a,b,c,d)
    print('#%i'%t,mx-mn)
