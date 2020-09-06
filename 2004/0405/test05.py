dataSource = [
    ["doc1", "t1", "t2", "t3"],
    ["doc2", "t0", "t2", "t3"],
    ["doc3", "t1", "t6", "t7"],
    ["doc4", "t1", "t2", "t4"],
    ["doc5", "t6", "t100", "t8"]
]

tags = ["t1", "t2", "t3"]

def solution(dataSource, tags):
    n=len(dataSource)
    for i in range(n):
        cnt=0
        for j in tags:
            if j in dataSource[i]:
                cnt+=1
        dataSource[i].append(cnt)
    dataSource=sorted(dataSource, key=lambda x:x[-1],reverse=True)
    answer=[i[0] for i in dataSource if i[-1]!=0]
    return answer[:10]

print(solution(dataSource,tags))