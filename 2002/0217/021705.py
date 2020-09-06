import time
start=time.time()

def backtrack(a,k,input,s):
    if k==input:
        if s==10:
            for i in range(input):
                if a[i]==1:
                    print(P[i],end=" ")
            print()
    else:
        if s<=10:
            a[k]=0
            backtrack(a,k+1,input,s)
            a[k]=1
            backtrack(a,k+1,input,s+P[k])

a=[0]*100
P=list(range(1,11))
backtrack(a,0,10,0)

print('time :',time.time()-start)