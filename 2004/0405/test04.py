snapshots = [
  ["ACCOUNT1", "100"],
  ["ACCOUNT2", "150"],
  ["ACCOUNT10", "150"]
]
transactions = [
  ["1", "SAVE", "ACCOUNT2", "100"],
  ["2", "WITHDRAW", "ACCOUNT1", "50"],
  ["1", "SAVE", "ACCOUNT2", "100"],
  ["4", "SAVE", "ACCOUNT3", "500"],
  ["3", "WITHDRAW", "ACCOUNT2", "30"]
]

# result = [
#   ["ACCOUNT1", "50"],
#   ["ACCOUNT10", "150"],
#   ["ACCOUNT2", "220"],
#   ["ACCOUNT3", "500"]
# ]

def solution(snapshots,transactions):
    transactions2=[]
    for i in transactions:
        if i not in transactions2:
            transactions2.append(i)
    result=[]
    for i in snapshots:
        result.append(i)
    for i in transactions2:
        z=0
        for j in result:
            if i[2]==j[0]:
                if i[1]=='SAVE':
                    j[1]=str(int(j[1])+int(i[3]))
                if i[1]=='WITHDRAW':
                    j[1]=str(int(j[1])-int(i[3]))
                z=1
            if z:
                break
        else:
            result.append([i[2],i[3]])
    return result

print(solution(snapshots,transactions))