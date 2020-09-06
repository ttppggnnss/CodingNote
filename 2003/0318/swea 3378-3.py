import sys
sys.stdin=open('input.txt','r')

from itertools import product as pr

def check(x):
    global a, b, c, d, e, f
    a += x.count('(')
    b += x.count(')')
    c += x.count('{')
    d += x.count('}')
    e += x.count('[')
    f += x.count(']')
    return [a, b, c, d, e, f]


tn = int(input())
for ir in range(tn):
    M, N = map(int, input().split())
    A = [list(input()) for i__1 in range(M)]
    B = [list(input()) for i_1 in range(N)]
    A_num = []
    a, b, c, d, e, f = 0, 0, 0, 0, 0, 0
    for i in range(len(A)):
        cnt = 0
        for i1 in range(len(A[i])):
            if A[i][i1] == '.':
                cnt += 1
            else:
                break
        if 1 <= i:
            a, b, c, d, e, f = check(A[i - 1])
            A_num.append([cnt, a - b, c - d, e - f])

    R_1, C_1, S_1 = 0, 0, 0
    for ii_2 in A_num:
        R_1 += ii_2[1]
        C_1 += ii_2[2]
        S_1 += ii_2[3]
    R, C, S = list(range(1, 21)), list(range(1, 21)), list(range(1, 21))
    if R_1 == 0:
        R = [-50]

    if C_1 == 0:
        C = [-50]

    if S_1 == 0:
        S = [-50]

    re = []
    for iii in A_num:
        if sum(iii) != 0:
            ch_l = iii[:]
    R1, C1, S1 = ch_l[1], ch_l[2], ch_l[3]
    for i1 in R:
        for j1 in C:
            for k1 in S:
                if ch_l[0] == (R1 * i1) + (C1 * j1) + (S1 * k1):
                    re.append([i1, j1, k1])

    result = []
    while re:
        v = re.pop(-1)
        for ii_1 in A_num:
            if ii_1[0] != ii_1[1] * v[0] + ii_1[2] * v[1] + ii_1[3] * v[2]:
                break
        else:
            result.append(v)
    if len(result) == 0:
        result = [[-50, -50, -50]]
    # print(result)

    B_num = []
    a, b, c, d, e, f = 0, 0, 0, 0, 0, 0
    for i in range(len(B)):
        if 1 <= i:
            a, b, c, d, e, f = check(B[i - 1])
            B_num.append([a - b, c - d, e - f])
    # print(B_num)
    final = []
    for ii_3 in range(len(B_num)):
        a7, b7, c7 = B_num[ii_3][0], B_num[ii_3][1], B_num[ii_3][2]
        fi_n = []
        for ii_4 in range(len(result)):
            fi_n.append(result[ii_4][0] * a7 + result[ii_4][1] * b7 + result[ii_4][2] * c7)

        fi_n = set(fi_n)
        fi_n = list(fi_n)
        if len(fi_n) != 1:
            final.append(-1)
        elif fi_n[0] < 0:
            final.append(-1)
        else:
            final += fi_n
    print('#{} 0 '.format(ir + 1), end='')
    for i in range(len(final)):
        print('{}'.format(final[i]), end=' ')
    print()