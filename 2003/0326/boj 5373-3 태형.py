import sys
sys.stdin=open('../input.txt','r')

T = int(input())
for t in range(T):
    N = int(input())
    rotate = [i for i in input().split()]

    cube = []
    tempcube = []
    cube.append([['w'] * 3 for _ in range(3)])
    cube.append([['y'] * 3 for _ in range(3)])
    cube.append([['r'] * 3 for _ in range(3)])
    cube.append([['o'] * 3 for _ in range(3)])
    cube.append([['g'] * 3 for _ in range(3)])
    cube.append([['b'] * 3 for _ in range(3)])
    tempcube.append([['w'] * 3 for _ in range(3)])
    tempcube.append([['y'] * 3 for _ in range(3)])
    tempcube.append([['r'] * 3 for _ in range(3)])
    tempcube.append([['o'] * 3 for _ in range(3)])
    tempcube.append([['g'] * 3 for _ in range(3)])
    tempcube.append([['b'] * 3 for _ in range(3)])


    def U(k):
        if k == '+':
            cube[2][0] = tempcube[5][0][:]
            cube[3][0] = tempcube[4][0][:]
            cube[4][0] = tempcube[2][0][:]
            cube[5][0] = tempcube[3][0][:]
        else:
            cube[2][0] = tempcube[4][0][:]
            cube[3][0] = tempcube[5][0][:]
            cube[4][0] = tempcube[3][0][:]
            cube[5][0] = tempcube[2][0][:]
        for k in range(6):
            tempcube[k][0] = cube[k][0][:]


    def D(k):
        if k == '+':
            cube[2][2] = tempcube[4][2][:]
            cube[3][2] = tempcube[5][2][:]
            cube[4][2] = tempcube[3][2][:]
            cube[5][2] = tempcube[2][2][:]
        else:
            cube[2][2] = tempcube[5][2][:]
            cube[3][2] = tempcube[4][2][:]
            cube[4][2] = tempcube[2][2][:]
            cube[5][2] = tempcube[3][2][:]
        for k in range(6):
            tempcube[k][2] = cube[k][2][:]


    def F(k):
        if k == '+':
            for k in range(3):
                cube[0][2][k] = tempcube[4][k][2]
                cube[1][0][k] = tempcube[5][k][0]
                cube[4][k][2] = tempcube[1][0][k]
                cube[5][k][0] = tempcube[0][2][k]
            for k in range(3):
                tempcube[0][2][k] = cube[0][2][k]
                tempcube[1][0][k] = cube[1][0][k]
                tempcube[4][k][2] = cube[4][k][2]
                tempcube[5][k][0] = cube[5][k][0]
        else:
            for k in range(3):
                cube[0][2][k] = tempcube[5][k][0]
                cube[1][0][k] = tempcube[4][k][2]
                cube[4][k][2] = tempcube[0][2][k]
                cube[5][k][0] = tempcube[1][0][k]
            for k in range(3):
                tempcube[0][2][k] = cube[0][2][k]
                tempcube[1][0][k] = cube[1][0][k]
                tempcube[4][k][2] = cube[4][k][2]
                tempcube[5][k][0] = cube[5][k][0]


    def B(k):
        if k == '+':
            for k in range(3):
                cube[0][0][k] = tempcube[5][k][2]
                cube[1][2][k] = tempcube[4][k][0]
                cube[4][k][0] = tempcube[0][0][k]
                cube[5][k][2] = tempcube[1][2][k]
            for k in range(3):
                tempcube[0][0][k] = cube[0][0][k]
                tempcube[1][2][k] = cube[1][2][k]
                tempcube[4][k][0] = cube[4][k][0]
                tempcube[5][k][2] = cube[5][k][2]
        else:
            for k in range(3):
                cube[0][0][k] = tempcube[4][k][0]
                cube[1][2][k] = tempcube[5][k][2]
                cube[4][k][0] = tempcube[1][2][k]
                cube[5][k][2] = tempcube[0][0][k]
            for k in range(3):
                tempcube[0][0][k] = cube[0][0][k]
                tempcube[1][2][k] = cube[1][2][k]
                tempcube[4][k][0] = cube[4][k][0]
                tempcube[5][k][2] = cube[5][k][2]


    def L(k):
        if k == '+':
            for k in range(3):
                cube[0][k][0] = tempcube[3][k][2]
                cube[1][k][0] = tempcube[2][k][0]
                cube[2][k][0] = tempcube[0][k][0]
                cube[3][k][2] = tempcube[1][k][0]
            for k in range(3):
                tempcube[0][k][0] = cube[0][k][0]
                tempcube[1][k][0] = cube[1][k][0]
                tempcube[2][k][0] = cube[2][k][0]
                tempcube[3][k][2] = cube[3][k][2]
        else:
            for k in range(3):
                cube[0][k][0] = tempcube[2][k][0]
                cube[1][k][0] = tempcube[3][k][2]
                cube[2][k][0] = tempcube[1][k][0]
                cube[3][k][2] = tempcube[0][k][0]
            for k in range(3):
                tempcube[0][k][0] = cube[0][k][0]
                tempcube[1][k][0] = cube[1][k][0]
                tempcube[2][k][0] = cube[2][k][0]
                tempcube[3][k][2] = cube[3][k][2]


    def R(k):
        if k == '+':
            for k in range(3):
                cube[0][k][2] = tempcube[2][k][2]
                cube[1][k][2] = tempcube[3][k][0]
                cube[2][k][2] = tempcube[1][k][2]
                cube[3][k][0] = tempcube[0][k][2]
            for k in range(3):
                tempcube[0][k][2] = cube[0][k][2]
                tempcube[1][k][2] = cube[1][k][2]
                tempcube[2][k][2] = cube[2][k][2]
                tempcube[3][k][0] = cube[3][k][0]
        else:
            for k in range(3):
                cube[0][k][2] = tempcube[3][k][0]
                cube[1][k][2] = tempcube[2][k][2]
                cube[2][k][2] = tempcube[0][k][2]
                cube[3][k][0] = tempcube[1][k][2]
            for k in range(3):
                tempcube[0][k][2] = cube[0][k][2]
                tempcube[1][k][2] = cube[1][k][2]
                tempcube[2][k][2] = cube[2][k][2]
                tempcube[3][k][0] = cube[3][k][0]


    for i in range(N):
        if rotate[i][0] == 'U':
            U(rotate[i][1])
        elif rotate[i][0] == 'D':
            D(rotate[i][1])
        elif rotate[i][0] == 'F':
            F(rotate[i][1])
        elif rotate[i][0] == 'B':
            B(rotate[i][1])
        elif rotate[i][0] == 'L':
            L(rotate[i][1])
        elif rotate[i][0] == 'R':
            R(rotate[i][1])

    for i in range(3):
        print(*cube[0][i],sep="")