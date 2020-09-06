a=[69,10,30,2,16,8,31,22]

def quickSort(a,begin,end):
    if begin<end:
        print()
        p=partition(a,begin,end)
        print(a[p])
        print(a[:p])
        print(a[p + 1:])
        quickSort(a,begin,p-1)
        quickSort(a,p+1,end)

def partition(a,begin,end):
    pivot=(begin+end)//2
    while begin < end:
        while a[begin]<a[pivot] and begin<end:
            begin+=1
        while a[end]>=a[pivot] and begin<end:
            end-=1
        if begin<end:
            if begin==pivot:
                pivot=end
            a[begin],a[end]=a[end],a[begin]
    a[pivot],a[end]=a[end],a[pivot]
    return end

quickSort(a,0,len(a)-1)

print(a)
