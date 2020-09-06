from itertools import combinations as c

def solution(answer_sheet, sheets):
    ans=0
    for i in c(sheets,2):
        cnt=0
        con=0
        concnt=0
        for j in range(len(answer_sheet)):
            k=0
            if i[0][j]==i[1][j] and i[0][j]!=answer_sheet[j]:
                cnt+=1
                k=1
            if k==1:
                con+=1
                concnt=max(con,concnt)
            else:
                con=0
        res=cnt+concnt**2
        ans=max(ans,res)
    return ans