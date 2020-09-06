import sys
sys.stdin=open('../input.txt','r')

n=int(input())
a=int(input())
RSP=[*input()]
RSP.insert(a,'W')
RSP2=[]
candi=[]
while len(RSP)>1:
    n=len(RSP)
    for i in range(n//2):
        if RSP[2*i]=='W':
            RSP2.append('W')
            candi.append(RSP[2*i+1])
        elif RSP[2*i+1]=='W':
            RSP2.append('W')
            candi.append(RSP[2*i])
        elif (RSP[2*i],RSP[2*i+1]) in [('R','P'),('S','R'),('P','S')]:
            RSP2.append(RSP[2*i+1])
        elif (RSP[2*i],RSP[2*i+1]) in [('P','R'),('R','S'),('S','P')]:
            RSP2.append(RSP[2*i])
        else:
            pass
    if n&1:
        RSP2.append(RSP[-1])
    RSP=RSP2[:]
    RSP2=[]
print(candi)
candi2=[candi[0]]
for i in candi:
    if i==candi2[-1]:
        pass
    else:
        candi2.append(i)
ans=len(candi2)-1
print(ans)