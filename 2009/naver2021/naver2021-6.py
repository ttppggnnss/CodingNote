# 기업 매칭

ex1 = ["A fabdec 2", "B cebdfa 2", "C ecfadb 2"],	["a BAC 1", "b BAC 3", "c BCA 2", "d ABC 3", "e BCA 3", "f ABC 2"]
# ["A_bf", "B_ce", "C_d"]
ex2 = ["A abc 2", "B abc 1"],	["a AB 1", "b AB 1", "c AB 1"]
# ["A_ab", "B_"]

def solution(companies, applicants):
    answer = []

    companies_dic = dict()
    for i in companies:
        name, order, count = i.split()
        companies_dic[name] = [[], [*order], int(count)]

    applicants_dic = dict()
    for i in applicants:
        name, order, count = i.split()
        applicants_dic[name] = [*order][:int(count)][::-1]


    # print(companies_dic)
    # print(applicants_dic)
    rejected = list(key for key in applicants_dic.keys())
    while rejected:

        for k in rejected:
            try:
                company = applicants_dic[k].pop()
                companies_dic[company][0].append(k)
            except:
                continue
        rejected = []

        for k, v in companies_dic.items():
            v[0].sort(key=lambda x:v[1].index(x))
            rejected += v[0][v[2]:]
            v[0] = v[0][:v[2]]
            v[0].sort()


    # print(companies_dic)
    for k,v in companies_dic.items():
        answer.append(k+'_'+''.join(v[0]))

    return answer


print(solution(*ex2))