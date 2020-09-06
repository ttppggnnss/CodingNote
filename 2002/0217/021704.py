import time
start=time.time()

def backtrack(a,k,input):
    if k==input:
        psum=0
        for i in range(input):
            if a[i]==1:
                psum+=P[i]
        if psum==10:
            for i in range(input):
                if a[i]==1:
                    print(P[i],end=" ")
            print()
        return
    else:
        a[k]=0
        backtrack(a,k+1,input)
        a[k]=1
        backtrack(a,k+1,input)

a=[0]*10
P=list(range(1,11))
backtrack(a,0,10)


print('time :',time.time()-start)

