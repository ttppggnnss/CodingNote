import sys
sys.stdin=open('../input.txt','r')

def findParents(r, prnV):
	root=r
	while parent[root] !=-1:
		prnV.append(parent[root])
		root=parent[root]

def getCommRoot():
	global x, y
	prnX = []
	prnY = []
	prnX.append(x)
	prnY.append(y)

	findParents(x,prnX)
	findParents(y,prnY)
	commRoot=0
	for i in range(len(prnX)):
		for j in range(len(prnY)):
			if prnX[i]==prnY[j]:
				commRoot=prnX[i]
				return commRoot
	return commRoot

n=int(input())
ch=input()
x,y=map(int,input().split())

parent=[-1]*99999
idx=[-1]*99999
idx[0]=0

st=[]
j=0
for i in range(len(ch)):
	if j==0:
		parent[j]=-1
		j+=1
		st.append(j)
		idx[j]=st[-1]
	else:
		if ch[i]=='0':
			prn=st[-1]
			parent[j]=prn
			j+=1
			st.append(j)
			idx[i]=st[-1]
		elif ch[i]=='1':
			idx[i]=st[-1]
			st.pop()
x=idx[x-1]
y=idx[y-1]
commRoot = getCommRoot()


for i in range(len(ch)):
	if idx[i]==commRoot:
		print(i+1)
		break

i=2*n-1
while i>=0:
	if idx[i]==commRoot:
		print(i+1)
		break
	i-=1
