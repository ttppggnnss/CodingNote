import sys
sys.stdin=open('../input.txt','r')

dic={'U':0,'D':1,'F':2,'B':3,'L':4,'R':5}
def main_rotate(a):
    global c
    c[9*a],c[9*a+1],c[9*a+2],c[9*a+3],c[9*a+4],c[9*a+5],c[9*a+6],c[9*a+7],c[9*a+8]=\
        c[9*a+6],c[9*a+3],c[9*a],c[9*a+7],c[9*a+4],c[9*a+1],c[9*a+8],c[9*a+5],c[9*a+2]

def sub_rotate(b):
    global c
    if b=='U':
        c[29],c[28],c[27],c[47],c[46],c[45],c[20],c[19],c[18],c[38],c[37],c[36]=\
        c[38],c[37],c[36],c[29],c[28],c[27],c[47],c[46],c[45],c[20],c[19],c[18]
    if b=='D':
        c[24],c[25],c[26],c[51],c[52],c[53],c[33],c[34],c[35],c[42],c[43],c[44]=\
        c[42],c[43],c[44],c[24],c[25],c[26],c[51],c[52],c[53],c[33],c[34],c[35]
    if b=='F':
        c[6],c[7],c[8],c[45],c[48],c[51],c[11],c[10],c[9],c[44],c[41],c[38]=\
        c[44],c[41],c[38],c[6],c[7],c[8],c[45],c[48],c[51],c[11],c[10],c[9]
    if b=='B':
        c[2],c[1],c[0],c[36],c[39],c[42],c[15],c[16],c[17],c[53],c[50],c[47]=\
        c[53],c[50],c[47],c[2],c[1],c[0],c[36],c[39],c[42],c[15],c[16],c[17]
    if b=='L':
        c[0],c[3],c[6],c[18],c[21],c[24],c[9],c[12],c[15],c[35],c[32],c[29]=\
        c[35],c[32],c[29],c[0],c[3],c[6],c[18],c[21],c[24],c[9],c[12],c[15]
    if b=='R':
        c[8],c[5],c[2],c[27],c[30],c[33],c[17],c[14],c[11],c[26],c[23],c[20]=\
        c[26],c[23],c[20],c[8],c[5],c[2],c[27],c[30],c[33],c[17],c[14],c[11]

for _ in range(int(input())):
    c=['w']*9+['y']*9+['r']*9+['o']*9+['g']*9+['b']*9
    n=int(input())
    o=input().split()
    for i in o:
        a=dic[i[0]]
        b=i[0]
        if i[1]=='+':
            main_rotate(a)
            sub_rotate(b)
        else:
            main_rotate(a)
            main_rotate(a)
            main_rotate(a)
            sub_rotate(b)
            sub_rotate(b)
            sub_rotate(b)
    print(*c[0:3],sep="")
    print(*c[3:6],sep="")
    print(*c[6:9],sep="")