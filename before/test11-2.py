import sys;sys.stdin=open("input11.txt","r")

def getpartialmatch(N):
    m = len(N)
    pi = [0] * m
    begin = 1
    st = 0
    while begin + st < m:
        if N[begin + st] == N[st]:
            st += 1
            pi[begin + st - 1] = st
        else:
            if st == 0:
                begin += 1
            else:
                begin += st - pi[st - 1]
                st = pi[st - 1]
        # print(pi)
        # print(begin,st)
    return pi

# N = int(input())
sentence = input()
print(len(sentence) - getpartialmatch(sentence)[-1])
print(getpartialmatch(sentence))
# [-1, 0, 1, 0, 0, 1, 2, 3, 4, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [-1, 0, 1, 2, 0, 0, 1, 2, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]