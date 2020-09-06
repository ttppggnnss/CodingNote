def scatterPalindrome(strToEvaluate):
    answer=[]
    for i in strToEvaluate:
        n=len(i)
        res=0
        for j in range(n):
            for k in range(j+1,n+1):
                candi=i[j:k]
                cnt={}
                k=0
                for z in candi:
                    if cnt.get(z):
                        cnt[z]+=1
                        if cnt[z]&1:
                            k+=1
                        else:
                            k-=1
                    else:
                        cnt[z]=1
                        k+=1
                if k<2:
                    res+=1
                    print(candi)
        answer.append(res)
    return answer

print(scatterPalindrome(['bbrrg']))