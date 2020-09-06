import time
start=time.time()

def scatterPalindrome(strToEvaluate):
    answer=[]
    for i in strToEvaluate:
        n=len(i)
        res=0
        for j in range(n):
            candi={}
            for k in range(j,n):
                try:
                    del candi[i[k]]
                except:
                    candi[i[k]]=1
                if len(candi)<2:
                    res+=1
        answer.append(res)
    return answer

print(scatterPalindrome(['aabb','abc','bbarg']))
# print(scatterPalindrome(['abcdefghijklmnopqrstuvwxyz'*40]*100))
print(time.time()-start)