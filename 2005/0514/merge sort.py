def merge_sort(L):
    if len(L)==1: return L

    m = len(L)//2
    left = L[:m]
    right = L[m:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result =  []
    while len(left)>0 or len(right)>0:
        if len(left)>0 and len(right)>0:
            if left[0]<=right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        elif len(left)>0:
            result.append(left.pop(0))
        elif len(right)>0:
            result.append(right.pop(0))
    return result

L = [69, 10, 30, 2, 16, 8, 31, 22]

print(merge_sort(L))