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

a=[0]*5
P=[1,3,6,7,10]
backtrack(a,0,5)