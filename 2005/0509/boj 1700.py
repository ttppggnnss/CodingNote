import sys
sys.stdin=open('../input.txt', 'r')

n, k = map(int,input().split())
L = input().split()

tab=[0]*n
ans=0

for i in range(k):
    if L[i] in tab:
        pass
    elif 0 in tab:
        tab[tab.index(0)]=L[i]
    else:
        tab2=[]
        for j in tab:
            try:
                a=L[i:].index(j)
                tab2.append(a)
            except:
                a=9**9
                tab2.append(a)
                break
        b=tab2.index(max(tab2))
        tab[b]=L[i]
        ans+=1
print(ans)