import sys
sys.stdin=open('../input.txt','r')

def bf(a, p=[]):
    if len(p)==7:
        global ans
        if isone(p):
            A=[]
            for j in p:
                A.append(board[j])
            if A.count('S')>3:
                ans+=1
    else:
        for i in range(len(a)):
            p.append(a[i])
            bf(a[i+1:],p)
            p.pop()

di=[1,-1,0,0]
dj=[0,0,1,-1]
def isone(k):
    visit2=[0]*25
    i,j=divmod(k[0],5)
    visit2[i*5+j]=1
    q=[(i,j)]
    while q:
        i,j=q.pop()
        for z in range(4):
            ni,nj=i+di[z],j+dj[z]
            if -1<ni<5 and -1<nj<5 and visit2[ni*5+nj]<1 and (ni*5+nj in k):
                visit2[ni*5+nj]=1
                q.append((ni,nj))
    if sum(visit2)==7:
        return True
    else:
        return False

board=[]
for i in range(5):
    board.extend([*input()])
ans=0
a=list(range(25))
bf(a,[])
print(ans)