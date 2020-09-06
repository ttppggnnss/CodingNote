# 숏코딩
def s(l):
    n={0}
    for i in l:
        for j in list(n):n.add(j+i)
    return len(n)
for t in range(int(input())):
    input()
    print("#%d %d"%(t+1,s(list(map(int, input().split())))))