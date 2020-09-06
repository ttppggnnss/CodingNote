def A_F(code, l):
    global af
    a = 0  # (
    b = 0  # )
    c = 0  # {
    d = 0  # }
    e = 0  # [
    f = 0  # ]
    for i in range(0, l):
        for j in range(len(code[i])):
            if code[i][j] == '(':
                a += 1
            elif code[i][j] == ')':
                b += 1
            elif code[i][j] == '{':
                c += 1
            elif code[i][j] == '}':
                d += 1
            elif code[i][j] == '[':
                e += 1
            elif code[i][j] == ']':
                f += 1
        af.append((a - b, c - d, e - f))  # 괄호의 차 저장


def RCS(af, indenp, p):
    org = []
    ab, cd, ef = af[0]
    # if p==1:
    #    return org
    for R in range(1, 21):
        for C in range(1, 21):
            for S in range(1, 21):
                if p == 1:
                    org.append((R, C, S))
                elif R * ab + C * cd + S * ef == indenp[1]:
                    org.append((R, C, S))

    for i in range(2, p):
        ab, cd, ef = af[i - 1]
        dest = []
        for R, C, S in org:
            if R * ab + C * cd + S * ef == indenp[i]:
                dest.append((R, C, S))
        org = dest

    return org


T = int(input())
for tc in range(1, T + 1):
    p, q = map(int, input().split())
    indenp = [0] * p

    codep = []
    codeq = []

    for i in range(p):
        codep.append(input())
    for i in range(q):
        codeq.append(input())
    af = []
    A_F(codep, p)  # 괄호 개수

    for i in range(p):  # 들여쓰기 개수 확인
        cnt = 0
        while codep[i][cnt] == '.':
            cnt += 1
        indenp[i] = cnt

    # R, C, S 정하기
    rcs = RCS(af, indenp, p)

    # 들여쓰기 R(a-b) + C(c-d) + S(e-f)
    af = []  # 라인별 괄호 개수
    A_F(codeq, q)
    indenq = [0] * q
    for i in range(1, q):
        ab, cd, ef = af[i - 1]  # 이전 줄 까지의 괄호 개수를 이용해 들여쓰기 계산
        if rcs:
            R, C, S = rcs[0]
            ans = R * ab + C * cd + S * ef
            for x in rcs[1:]:
                R, C, S = x
                if R * ab + C * cd + S * ef != ans:
                    indenq[i] = -1
                    break
            if indenq[i] != -1:
                indenq[i] = ans
        else:
            indenq[i] = -1
            break
    print('#{}'.format(tc), end=' ')
    for x in indenq:
        print(x, end=' ')
    print()