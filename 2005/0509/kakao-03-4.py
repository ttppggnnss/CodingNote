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
# 시간초과

def solution(gems):
    candi=set(gems)
    ans=len(gems)
    answer=[1,ans]
    for i in range(len(gems)-1):
        for j in range(i,len(gems)):
            if j-i+1>ans:
                break
            for k in candi:
                if k not in gems[i-1:j]:
                    break
            else:
                if j-i+1<ans:
                    ans=j-i+1
                    answer=[i,j]
                elif j-i+1==ans:
                    if i<answer[0]:
                        answer=[i,j]
    return answer
print(solution(gems))
