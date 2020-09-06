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
# 실패
def solution(gems):
    candi=set(gems)
    ans=len(gems)
    answer=[1,ans]
    q=[]
    q.append((1,ans))
    while q:
        i,j=q.pop()
        for k in candi:
            if k not in gems[i-1:j]:
                break
        else:
            if j-i+1<ans:
                ans=j-i+1
                answer=[i,j]
                q.append((i + 1, j))
                q.append((i, j - 1))
            elif j-i+1==ans:
                if i<answer[0]:
                    answer=[i,j]
                q.append((i + 1, j))
                q.append((i, j - 1))

    return answer
print(solution(gems))
