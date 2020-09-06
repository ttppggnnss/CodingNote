gems=["XYZ", "XYZ", "XYZ"]
'''
gems
["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
["AA", "AB", "AC", "AA", "AC"]
["XYZ", "XYZ", "XYZ"]
["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
result
[3,7]
[1,3]
[1,1]
[1,5]
'''
def solution(gems):
    candi=set(gems)
    m=len(candi)
    ans=len(gems)
    answer=[1,ans]
    if ans==m:
        return answer
    for i in range(1,len(gems)-m+1):
        for j in range(i+m-1,len(gems)+1):
            if ans==m:
                return answer
            if j-i+1>=ans:
                break
            for k in candi:
                if k not in gems[i-1:j]:
                    break
            else:
                if j-i+1<ans:
                    ans=j-i+1
                    answer=[i,j]
        if ans==m:
            return answer
    return answer
print(solution(gems))
