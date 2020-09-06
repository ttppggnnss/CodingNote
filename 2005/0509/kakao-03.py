gems= ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
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
    ans=len(gems)
    def solve(gems2,i,j,ans):
        for k in candi:
            if k not in gems2:
                return
        else:
            if len(gems2)<=ans:
                ans=len(gems2)
                global answer
                answer=[i,j]
                solve(gems2[1:], i + 1, j,ans)
                solve(gems2[:-1], i, j - 1,ans)
                return answer
    solve(gems,1,len(gems),ans)
    return answer
print(solution(gems))
